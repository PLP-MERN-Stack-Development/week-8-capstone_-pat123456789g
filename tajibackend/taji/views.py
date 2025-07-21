
# taji/views.py should have these imports at minimum:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MedicalRecordSerializer, AppointmentSerializer
from .models import MedicalRecord, Appointment
from django.contrib.auth import get_user_model


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalRecordList(generics.ListCreateAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]  # Now this will work

    def get_queryset(self):
        return MedicalRecord.objects.filter(patient=self.request.user)

class AppointmentView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]  # Add permission here too

    def get_queryset(self):
        if self.request.user.user_type == 'D':
            return Appointment.objects.filter(doctor=self.request.user)
        return Appointment.objects.filter(patient=self.request.user)