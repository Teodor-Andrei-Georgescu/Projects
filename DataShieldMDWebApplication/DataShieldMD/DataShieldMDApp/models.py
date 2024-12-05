from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the auth_user table
    filename = models.CharField(max_length=255)  # Original file name
    upload_date = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
    file_path = models.CharField(max_length=255)  # Path to the uploaded file

    def __str__(self):
        return f"{self.filename} (Uploaded by: {self.user.username})"


class AlgorithmParameter(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)  # Links to the Datasets table
    algorithm_type = models.CharField(max_length=3)  # Example: 'K', 'KL', or 'KLT'
    k_anonymity_k_value = models.IntegerField(null=True, blank=True)  # Optional for k-anonymity
    l_value = models.IntegerField(null=True, blank=True)  # Optional for l-diversity
    l_diversity_k_value = models.IntegerField(null=True, blank=True)
    t_value = models.FloatField(null=True, blank=True)  # Optional for t-closeness
    t_closeness_k_value = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure `algorithm_type` is always ordered as "K", "L", "T"
        self.algorithm_type = ''.join(sorted(self.algorithm_type, key=lambda x: 'KLT'.index(x)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Parameters for Dataset {self.dataset.filename} - {self.algorithm_type}"

class ProcessedDataset(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)  # Links to the Datasets table
    algorithm_type = models.CharField(max_length=1)  #'k' for k-anonymity, 'l' for l-diversity, or 't' for t-closeness
    processed_file_path = models.CharField(max_length=255)  # Path to the processed file
    processed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Processed {self.dataset.filename} with {self.algorithm_type}"


class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the auth_user table
    action = models.CharField(max_length=20)  # e.g., 'upload', 'process', 'download'
    action_date = models.DateTimeField(auto_now_add=True)  # Timestamp of the action
    action_success = models.BooleanField()  # Whether the action was successful

    def __str__(self):
        return f"Action {self.action} by {self.user.username} on {self.action_date}"