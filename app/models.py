# models.py
from arrow import now
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username



# class ServiceRequest(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('resolved', 'Resolved'),
#     ]

    # service_type = models.CharField(max_length=255, help_text="Name of the service request")
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # resolved_at = models.DateTimeField(null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    # attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    # created_at = models.DateTimeField(default=datetime(2025, 1, 1, 12, 12, 1))  # Fixed datetime for created_at
    # updated_at = models.DateTimeField(default=datetime(2025, 1, 1, 12, 12, 1))

   


from django.db import models

class ServiceRequest(models.Model):
    
    SERVICE_TYPE_CHOICES = [
        ('Gas', 'Gas Leakage'),
        ('Gaspipeline', 'Gas Pipeline Leakage'),
        ('Cylinder', 'Cylinder Nozzle Break'),
        ('Billing', 'Billing Issue'),
    ]

    service_type = models.CharField(max_length=100,choices=SERVICE_TYPE_CHOICES)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.name


