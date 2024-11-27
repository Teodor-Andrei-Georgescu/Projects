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
    algorithm_type = models.CharField(max_length=3)  #'k' for k-anonymity, 'l' for l-diversity, or 't' for t-closeness
    k_value = models.IntegerField(null=True, blank=True)  # Optional for k-anonymity
    l_value = models.IntegerField(null=True, blank=True)  # Optional for l-diversity
    t_value = models.IntegerField(null=True, blank=True)  # Optional for t-closeness

    def __str__(self):
        return f"Parameters for Dataset {self.dataset.filename} - {self.algorithm_type}"


class ProcessedDataset(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)  # Links to the Datasets table
    algorithm_type = models.CharField(max_length=3)  #'k' for k-anonymity, 'l' for l-diversity, or 't' for t-closeness
    processed_file_path = models.CharField(max_length=255)  # Path to the processed file

    def __str__(self):
        return f"Processed {self.dataset.filename} with {self.algorithm_type}"


class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the auth_user table
    action = models.CharField(max_length=20)  # e.g., 'upload', 'process', 'download'
    action_date = models.DateTimeField(auto_now_add=True)  # Timestamp of the action
    action_success = models.BooleanField()  # Whether the action was successful

    def __str__(self):
        return f"Action {self.action} by {self.user.username} on {self.action_date}"