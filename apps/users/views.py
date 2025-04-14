from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import PermissionDenied

from .models import User, DoctorProfile, PatientProfile, StaffProfile
from .serializers import (
    UserSerializer,
    DoctorProfileSerializer,
    PatientProfileSerializer,
    StaffProfileSerializer,
    MyTokenObtainPairSerializer
)


# ============================
# Custom Role-Based Permission
# ============================
class IsAdminOrRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Admin has access to everything
        if request.user.role == 'admin':
            return True

        # Role-based access for own profile
        role_access = {
            'doctor': 'doctors',
            'patient': 'patients',
            'staff': 'staff'
        }

        return view.basename == role_access.get(request.user.role)


# ======================
# User CRUD (Register + Admin View)
# ======================
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsAdminOrRole()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully.",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ======================
# Role-Based Profile Views
# ======================
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrRole]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return DoctorProfile.objects.all()
        return DoctorProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        # Ensure only doctors can create doctor profiles
        if self.request.user.role != 'doctor':
            raise PermissionDenied("Only users with the doctor role can create doctor profiles.")
        serializer.save(user=self.request.user)



class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrRole]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return PatientProfile.objects.all()
        return PatientProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrRole]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return StaffProfile.objects.all()
        return StaffProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        if self.request.user.role != 'staff':
            raise PermissionDenied("Only users with the staff role can create staff profiles.")
        serializer.save(user=self.request.user)


# ======================
# Signup View (Optional - Used if not using ViewSet create)
# ======================
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ======================
# Custom Login View with Token
# ======================
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ======================
# Logout View - Blacklist Token
# ======================
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
