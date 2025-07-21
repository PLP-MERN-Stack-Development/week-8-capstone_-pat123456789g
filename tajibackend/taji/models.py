# taji/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
      # Add these to resolve the conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="taji_user_set",  # Changed from default
        related_query_name="taji_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="taji_user_set",  # Changed from default
        related_query_name="taji_user",
    )

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_records')
    diagnosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ))
    notes = models.TextField(blank=True)