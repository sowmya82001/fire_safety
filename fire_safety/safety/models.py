from django.db import models
from django.contrib.auth.models import User

class OTPStorage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    
from django.db import models

# Fire Detection Module
class FireIncident(models.Model):
    location = models.CharField(max_length=255)
    severity = models.CharField(max_length=50, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    detected_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Active", "Active"), ("Resolved", "Resolved")])

    def __str__(self):
        return f"{self.location} - {self.severity} - {self.status}"

# Emergency Response Module
class EmergencyResponse(models.Model):
    fire_incident = models.ForeignKey(FireIncident, on_delete=models.CASCADE)
    responders_notified = models.BooleanField(default=False)
    evacuation_status = models.CharField(max_length=50, choices=[("Not Started", "Not Started"), ("In Progress", "In Progress"), ("Completed", "Completed")])

    def __str__(self):
        return f"{self.fire_incident.location} - {self.evacuation_status}"

# Training & Awareness Module
class FireTraining(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    participants = models.IntegerField()

    def __str__(self):
        return self.title

# Evacuation & Compliance Module
class ComplianceCheck(models.Model):
    location = models.CharField(max_length=255)
    inspection_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Pass", "Pass"), ("Fail", "Fail")])
    remarks = models.TextField()

    def __str__(self):
        return f"{self.location} - {self.status}"
