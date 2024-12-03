from django.conf import settings
import os
from jnius import autoclass

# Load Java classes
ARXAnonymizer = autoclass('org.deidentifier.arx.ARXAnonymizer')
Data = autoclass('org.deidentifier.arx.Data')
DataType = autoclass('org.deidentifier.arx.DataType')

class ARXWrapper:
    @staticmethod
    def load_data(file_path, identifying_fields, sensitive_fields):
        """Load data from file and define identifying/sensitive fields."""
        data = Data.create(file_path)
        for field in identifying_fields.split(','):
            data.getDefinition().setAttributeType(field.strip(), Data.AttributeType.QUASI_IDENTIFYING)
        for field in sensitive_fields.split(','):
            data.getDefinition().setAttributeType(field.strip(), Data.AttributeType.SENSITIVE)
        return data

    @staticmethod
    def apply_k_anonymity(data, k_value):
        """Apply k-anonymity."""
        anonymizer = ARXAnonymizer()
        anonymizer.anonymize(data, Data.createConfiguration(k_value))
        return data

    @staticmethod
    def apply_l_diversity(data, l_value):
        """Apply l-diversity."""
        anonymizer = ARXAnonymizer()
        config = Data.createConfiguration()
        config.addPrivacyModel(autoclass('org.deidentifier.arx.privacy.LDiversity')(l_value))
        anonymizer.anonymize(data, config)
        return data

    @staticmethod
    def apply_t_closeness(data, t_value):
        """Apply t-closeness."""
        anonymizer = ARXAnonymizer()
        config = Data.createConfiguration()
        config.addPrivacyModel(autoclass('org.deidentifier.arx.privacy.TCloseness')(t_value))
        anonymizer.anonymize(data, config)
        return data

    @staticmethod
    def save_data(data, output_file_path):
        """Save processed data to output file."""
        with open(output_file_path, 'w') as f:
            iterator = data.iterator()
            while iterator.hasNext():
                f.write(','.join(iterator.next()))
                f.write('\n')