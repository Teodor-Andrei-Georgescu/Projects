import pandas as pd
import anonypy
import numpy as np

'''
Works but not necessarily as expected but seems to be the best I can do.

Also this I had to make a change to the libary files in my venv to get it to work.
So I am pasting my venv's version of the library files so it actually runs.

my anonypy.py:
from anonypy import mondrian
import pandas as pd


class Preserver:
    def __init__(self, df, feature_columns, sensitive_column):
        self.modrian = mondrian.Mondrian(df, feature_columns, sensitive_column)

    def __anonymize(self, k, l=0, p=0.0):
        partitions = self.modrian.partition(k, l, p)
        return anonymize(
            self.modrian.df,
            partitions,
            self.modrian.feature_columns,
            self.modrian.sensitive_column,
        )

    def anonymize_k_anonymity(self, k):
        return self.__anonymize(k)

    def anonymize_l_diversity(self, k, l):
        return self.__anonymize(k, l=l)

    def anonymize_t_closeness(self, k, p):
        return self.__anonymize(k, p=p)

    def __count_anonymity(self, k, l=0, p=0.0):
        partitions = self.modrian.partition(k, l, p)
        return count_anonymity(
            self.modrian.df,
            partitions,
            self.modrian.feature_columns,
            self.modrian.sensitive_column,
        )

    def count_k_anonymity(self, k):
        return self.__count_anonymity(k)

    def count_l_diversity(self, k, l):
        return self.__count_anonymity(k, l=l)

    def count_t_closeness(self, k, p):
        return self.__count_anonymity(k, p=p)


def agg_categorical_column(series):
    # this is workaround for dtype bug of series
    series.astype("category")

    l = [str(n) for n in set(series)]
    return [",".join(l)]


def agg_numerical_column(series):
    # return [series.mean()]
    minimum = series.min()
    maximum = series.max()
    if maximum == minimum:
        string = str(maximum)
    else:
        string = f"{minimum}-{maximum}"
    return [string]


def anonymize(df, partitions, feature_columns, sensitive_column, max_partitions=None):
    aggregations = {}
    for column in feature_columns:
        if df[column].dtype.name == "category":
            aggregations[column] = agg_categorical_column
        else:
            aggregations[column] = agg_numerical_column
    rows = []
    for i, partition in enumerate(partitions):
        if max_partitions is not None and i > max_partitions:
            break
        grouped_columns = df.loc[partition].agg(aggregations)  # Ensure proper aggregation
        sensitive_counts = (
            df.loc[partition]
            .groupby(sensitive_column, observed=False)
            .agg({sensitive_column: "count"})
        )
        if isinstance(grouped_columns, pd.Series):  # Ensure compatibility
            grouped_columns = grouped_columns.to_frame().T
        values = grouped_columns.iloc[0].to_dict()  # Convert to dict for appending
        for sensitive_value, count in sensitive_counts[sensitive_column].items():
            if count == 0:
                continue
            values.update(
                {
                    sensitive_column: sensitive_value,
                    "count": count,
                }
            )
            rows.append(values.copy())
    return rows




def count_anonymity(
    df, partitions, feature_columns, sensitive_column, max_partitions=None
):
    aggregations = {}
    for column in feature_columns:
        if df[column].dtype.name == "category":
            aggregations[column] = agg_categorical_column
        else:
            aggregations[column] = agg_numerical_column
    aggregations[sensitive_column] = "count"
    rows = []
    for i, partition in enumerate(partitions):
        if max_partitions is not None and i > max_partitions:
            break
        grouped_columns = df.loc[partition].agg(aggregations, squeeze=False)
        values = grouped_columns.iloc[0].to_dict()
        rows.append(values.copy())
    return rows

my mondrian.py file:

from anonypy import anonymity


class Mondrian:
    def __init__(self, df, feature_columns, sensitive_column=None):
        self.df = df
        self.feature_columns = feature_columns
        self.sensitive_column = sensitive_column

    def is_valid(self, partition, k=2, l=0, p=0.0):
        # k-anonymous
        if not anonymity.is_k_anonymous(partition, k):
            return False
        # l-diverse
        if l > 0 and self.sensitive_column is not None:
            diverse = anonymity.is_l_diverse(
                self.df, partition, self.sensitive_column, l
            )
            if not diverse:
                return False
        # t-close
        if p > 0.0 and self.sensitive_column is not None:
            global_freqs = anonymity.get_global_freq(self.df, self.sensitive_column)
            close = anonymity.is_t_close(
                self.df, partition, self.sensitive_column, global_freqs, p
            )
            if not close:
                return False

        return True

    def get_spans(self, partition, scale=None):
        spans = {}
        for column in self.feature_columns:
            if self.df[column].dtype.name == "category":
                span = len(self.df[column][partition].unique())
            else:
                span = (
                    self.df[column][partition].max() - self.df[column][partition].min()
                )
            if scale is not None:
                span = span / scale[column]
            spans[column] = span
        return spans

    def split(self, column, partition):
        dfp = self.df[column][partition]
        if dfp.dtype.name == "category":
            values = dfp.unique()
            lv = set(values[: len(values) // 2])
            rv = set(values[len(values) // 2 :])
            return dfp.index[dfp.isin(lv)], dfp.index[dfp.isin(rv)]
        else:
            median = dfp.median()
            dfl = dfp.index[dfp < median]
            dfr = dfp.index[dfp >= median]
            return (dfl, dfr)

    def partition(self, k=3, l=0, p=0.0):
        scale = self.get_spans(self.df.index)

        finished_partitions = []
        partitions = [self.df.index]
        while partitions:
            partition = partitions.pop(0)
            spans = self.get_spans(partition, scale)
            for column, span in sorted(spans.items(), key=lambda x: -x[1]):
                lp, rp = self.split(column, partition)
                if not self.is_valid(lp, k, l, p) or not self.is_valid(rp, k, l, p):
                    continue
                partitions.extend((lp, rp))
                break
            else:
                finished_partitions.append(partition)
        return finished_partitions


my anonymity.py:
def is_k_anonymous(partition, k):
    if len(partition) < k:
        return False
    return True


def is_l_diverse(df, partition, sensitive_column, l):
    diversity = len(df.loc[partition][sensitive_column].unique())
    return diversity >= l


def is_t_close(df, partition, sensitive_column, global_freqs, p):
    total_count = float(len(partition))
    d_max = None
    group_counts = (
        df.loc[partition].groupby(sensitive_column)[sensitive_column].agg("count")
    )
    for value, count in group_counts.to_dict().items():
        p = count / total_count
        d = abs(p - global_freqs[value])
        if d_max is None or d > d_max:
            d_max = d
    return d_max <= p


def get_global_freq(df, sensitive_column):
    global_freqs = {}
    total_count = float(len(df))
    group_counts = df.groupby(sensitive_column)[sensitive_column].agg("count")

    for value, count in group_counts.to_dict().items():
        p = count / total_count
        global_freqs[value] = p
    return global_freqs

'''


def read_data(data_path, sensitive_fields,):
    data = pd.read_csv(data_path)
    categorical = set()
    columns = []
    for column in data.columns:
        columns.append(column)
        if not pd.api.types.is_numeric_dtype(data[column]):
            categorical.add(column)
            
    for column in categorical:
        data[column] = data[column].astype('category')
        
    return data, columns
    
def apply_k_anonymity(data_path,sensitive_fields, k,output_path):
   
    data , columns = read_data(data_path,sensitive_fields)
    p = anonypy.Preserver(data, columns, sensitive_fields)
    rows = p.anonymize_k_anonymity(k)

    dfn = pd.DataFrame(rows)
    dfn.drop(["count"],axis=1, inplace=True)
    dfn.to_csv(output_path, index=False)

def apply_l_diversity(data_path,sensitive_fields,k,l,output_path):
    
    if k == None:
        k = l
    data , columns = read_data(data_path,sensitive_fields)
    p = anonypy.Preserver(data, columns, sensitive_fields)
    rows = p.anonymize_l_diversity(k,l)
    
    dfn = pd.DataFrame(rows)
    dfn.drop(["count"],axis=1, inplace=True)
    dfn.to_csv(output_path, index=False)
    
def apply_t_closeness(data_path, sensitive_fields, k, t, output_path):
    
    data , columns = read_data(data_path,sensitive_fields)
    p = anonypy.Preserver(data, columns, sensitive_fields)
    rows = p.anonymize_t_closeness(k,t)
    
    dfn = pd.DataFrame(rows)
    dfn.drop(["count"],axis=1, inplace=True)
    dfn.to_csv(output_path, index=False)
    
    
