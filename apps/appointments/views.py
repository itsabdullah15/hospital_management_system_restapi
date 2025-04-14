from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Appointment.objects.all()
        elif user.role == 'doctor':
            return Appointment.objects.filter(doctor=user)
        elif user.role == 'patient':
            return Appointment.objects.filter(patient=user)
        return Appointment.objects.none()


    def get_object(self):
        pk = self.kwargs["pk"]
        if self.request.user.role == 'admin':
            return get_object_or_404(Appointment, pk=pk)
        return super().get_object()



    def perform_create(self, serializer):
        if self.request.user.role != 'patient':
            raise PermissionDenied("Only patients can book appointments.")
        serializer.save(patient=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user != instance.patient and self.request.user.role != 'admin':
            raise PermissionDenied("You can only cancel your own appointments.")
        instance.delete()

    @action(detail=True, methods=['post'], url_path='accepted')
    def accept_appointment(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'accepted'
        appointment.save()
        return Response({'status': 'Appointment accepted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='rejected')
    def reject(self, request, pk=None):
        appointment = self.get_object()
        if request.user != appointment.doctor and request.user.role != 'admin':
            raise PermissionDenied("You are not allowed to reject this appointment.")
        appointment.status = 'rejected'
        appointment.save()
        return Response({'status': 'Appointment rejected'}, status=status.HTTP_200_OK)
