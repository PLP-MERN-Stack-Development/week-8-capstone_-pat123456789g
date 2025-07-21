# taji/serializers.py
from rest_framework import serializers
from .models import MedicalRecord, Appointment
# Add to taji/serializers.py
from django.contrib.auth import get_user_model
User = get_user_model()


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type', 'phone')