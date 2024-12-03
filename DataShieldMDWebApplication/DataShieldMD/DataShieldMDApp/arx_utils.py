from django.conf import settings
from jnius import autoclass

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


class ARXWrapper:
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
        
        return data

    
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

