from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalHistoryViewSet, PrescriptionViewSet, LabResultViewSet

router = DefaultRouter()
router.register('medical-history/', MedicalHistoryViewSet)
router.register('prescriptions/', PrescriptionViewSet)
router.register('lab-results/', LabResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
