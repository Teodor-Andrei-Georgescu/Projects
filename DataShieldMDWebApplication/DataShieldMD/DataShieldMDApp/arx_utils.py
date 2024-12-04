from django.conf import settings
from jnius import autoclass
'''
Spent alot of time on this but couldnt get the hierarchy to work so this is bascially worthless.
'''
# Load Java classes
ARXAnonymizer = autoclass('org.deidentifier.arx.ARXAnonymizer')
Data = autoclass('org.deidentifier.arx.Data')
AttributeType = autoclass('org.deidentifier.arx.AttributeType')
Charset = autoclass('java.nio.charset.Charset')
ARXConfiguration = autoclass('org.deidentifier.arx.ARXConfiguration')
KAnonymity = autoclass('org.deidentifier.arx.criteria.KAnonymity')
DistinctLDiversity = autoclass('org.deidentifier.arx.criteria.DistinctLDiversity')
EqualDistanceTCloseness = autoclass('org.deidentifier.arx.criteria.EqualDistanceTCloseness')
CSVSyntax = autoclass('org.deidentifier.arx.io.CSVSyntax')
DefaultHierarchy = autoclass('org.deidentifier.arx.AttributeType$Hierarchy$DefaultHierarchy')

#smt is clearl wrong here or I am doing smt wrong as things are anonimzying weirdly.
#I need to add hierachies I think
class ARXWrapper:
    @staticmethod
    def create_hierarchy_for_numerical(data_handle, attribute_name):
        """
        Create a numerical hierarchy using DefaultHierarchy for valid dataset values.
        """
        DefaultHierarchy = autoclass('org.deidentifier.arx.AttributeType$Hierarchy$DefaultHierarchy')

        # Find the column index for the attribute
        attribute_index = ARXWrapper.get_attribute_index(data_handle, attribute_name)

        # Extract numerical values for the attribute
        values = set(data_handle.getDistinctValues(attribute_index))
        numeric_values = sorted(float(v) for v in values)

        # Create the hierarchy
        hierarchy = DefaultHierarchy.create()
        step = 10  # Define the generalization step
        for value in numeric_values:
            generalized_value = f"{int(value // step * step)}-{int(value // step * step + step - 1)}"
            hierarchy.add(str(value), generalized_value, "*")

        return hierarchy

    
    @staticmethod
    def create_hierarchy_for_text(data_handle, attribute_name):
        """
        Create a text hierarchy using HierarchyBuilderRedactionBased.
        Generalizes text by masking characters.
        """
        HierarchyBuilderRedactionBased = autoclass('org.deidentifier.arx.aggregates.HierarchyBuilderRedactionBased')

        # Find the column index for the attribute
        attribute_index = ARXWrapper.get_attribute_index(data_handle, attribute_name)

        # Define hierarchy using HierarchyBuilder
        builder = HierarchyBuilderRedactionBased.create('*')
        values = set(data_handle.getDistinctValues(attribute_index))
        for value in values:
            builder.add(value)
        return builder.build()

    
    @staticmethod
    def generate_and_apply_hierarchies(data, quasi_identifiers):
        """
        Dynamically create and apply hierarchies for numerical and textual quasi-identifiers.
        """
        data_definition = data.getDefinition()
        data_handle = data.getHandle()

        for attribute in quasi_identifiers:
            # Dynamically determine the type of hierarchy
            if ARXWrapper.is_numeric(data_handle, attribute):
                hierarchy = ARXWrapper.create_hierarchy_for_numerical(data_handle, attribute)
            else:
                hierarchy = ARXWrapper.create_hierarchy_for_text(data_handle, attribute)

            print(f"Hierarchy class: {hierarchy.__class__}")
            # Apply the hierarchy
            data_definition.setAttributeType(attribute, hierarchy)

        return data

    @staticmethod
    def get_attribute_index(data_handle, attribute_name):
        """
        Find the column index for a given attribute name.
        """
        num_columns = data_handle.getNumColumns()
        for i in range(num_columns):
            if data_handle.getAttributeName(i) == attribute_name:
                return i
        raise ValueError(f"Attribute '{attribute_name}' not found in data handle.")

    @staticmethod
    def is_numeric(data_handle, attribute_name):
        """
        Determine if the attribute is numeric based on its distinct values.
        """
        attribute_index = ARXWrapper.get_attribute_index(data_handle, attribute_name)
        values = data_handle.getDistinctValues(attribute_index)
        try:
            # Try converting all values to floats
            [float(value) for value in values]
            return True
        except ValueError:
            return False
        
    @staticmethod
    def load_data(file_path, identifying_fields, sensitive_fields, k_anonmity):
        """Load data from a CSV file with UTF-8 encoding and proper CSV syntax."""
        charset = Charset.forName("UTF-8")

        # Create CSV syntax and set delimiter to comma
        csv_syntax = CSVSyntax()
        csv_syntax.setDelimiter(',')

        # Attempt to load the data with the correct ARX method
        data = Data.create(file_path, charset, csv_syntax, None)

        # Retrieve attributes from the data handle
        data_handle = data.getHandle()
        num_columns = data_handle.getNumColumns()
        attributes = [data_handle.getAttributeName(i) for i in range(num_columns)]
        print(f"Loaded attributes: {attributes}")

        # Normalize input fields
        sensitive_fields = [field.strip() for field in sensitive_fields.split(',')]
        identifying_fields = [field.strip() for field in identifying_fields.split(',')]

        # Assign attributes
        data_definition = data.getDefinition()
        
        for attr in attributes:
        # Default all attributes to insensitive
            data_definition.setAttributeType(attr, AttributeType.INSENSITIVE_ATTRIBUTE)
        
        for field in identifying_fields:
            if field in attributes:
                data_definition.setAttributeType(field, AttributeType.QUASI_IDENTIFYING_ATTRIBUTE)
            else:
                raise ValueError(f"Identifying field '{field}' not found in dataset columns: {attributes}")
        if not k_anonmity:
            for field in sensitive_fields:
                if field in attributes:
                    # Assign sensitive attributes, but K-anonymity won't enforce models on them
                    data_definition.setAttributeType(field, AttributeType.SENSITIVE_ATTRIBUTE)
                else:
                    raise ValueError(f"Sensitive field '{field}' not found in dataset columns: {attributes}")
        
        for attr in attributes:
            attr_type = data_definition.getAttributeType(attr).toString()
            print(f"Attribute: {attr}, Type: {attr_type}")
        
        return data,identifying_fields

    
    @staticmethod
    def apply_k_anonymity(data, k_value):
        """Apply K-Anonymity to the data."""
        try:
            # Create configuration for K-Anonymity
            config = ARXConfiguration.create()
            config.addPrivacyModel(KAnonymity(k_value))
            config.setSuppressionLimit(1)  # Allow full suppression if necessary

            # Apply the anonymization
            anonymizer = ARXAnonymizer()
            result = anonymizer.anonymize(data, config)

            # Verify results
            if not result.isResultAvailable():
                raise Exception("K-Anonymity anonymization failed.")
            
            return result.getOutput()

        except Exception as e:
            raise Exception(f"Error applying K-anonymity: {e}")

    @staticmethod
    def apply_l_diversity(data, l_value, sensitive_fields):
        """Apply L-Diversity to sensitive fields."""
        config = ARXConfiguration.create()
        for field in sensitive_fields.split(','):
            config.addPrivacyModel(DistinctLDiversity(field.strip(), l_value))
        config.setSuppressionLimit(1.0)

        anonymizer = ARXAnonymizer()
        result = anonymizer.anonymize(data, config)

        if not result.isResultAvailable():
            raise Exception("L-Diversity anonymization failed.")
        return result.getOutput()

    @staticmethod
    def apply_t_closeness(data, t_value, sensitive_fields):
        """Apply T-Closeness to sensitive fields."""
        config = ARXConfiguration.create()
        for field in sensitive_fields.split(','):
            config.addPrivacyModel(EqualDistanceTCloseness(field.strip(), t_value))
        config.setSuppressionLimit(1.0)

        anonymizer = ARXAnonymizer()
        result = anonymizer.anonymize(data, config)

        if not result.isResultAvailable():
            raise Exception("T-Closeness anonymization failed.")
        return result.getOutput()

    
    @staticmethod
    def save_data(data_handle, output_file_path):
        """Save processed data to an output file."""
        try:
            with open(output_file_path, 'w+', encoding='utf-8') as f:
                
                # Write data rows
                iterator = data_handle.iterator()
                while iterator.hasNext():
                    row = iterator.next()
                    f.write(','.join(row) + '\n')
            print(f"Data successfully saved to {output_file_path}")
        except Exception as e:
            raise Exception(f"Error saving data: {e}")

