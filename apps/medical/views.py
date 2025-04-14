from rest_framework import viewsets, permissions
from .models import MedicalHistory, Prescription, LabResult
from .serializers import (
    MedicalHistorySerializer,
    PrescriptionSerializer,
    LabResultSerializer
)

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow access to admin or the owner (patient)
        return request.user.role == 'admin' or obj.patient == request.user

class BasePatientRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return self.model.objects.all()
        return self.model.objects.filter(patient=user)

    def perform_create(self, serializer):
        if self.request.user.role == 'patient':
            serializer.save(patient=self.request.user)
        else:
            serializer.save()

class MedicalHistoryViewSet(BasePatientRecordViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    model = MedicalHistory

class PrescriptionViewSet(BasePatientRecordViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    model = Prescription

class LabResultViewSet(BasePatientRecordViewSet):
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer
    model = LabResult
