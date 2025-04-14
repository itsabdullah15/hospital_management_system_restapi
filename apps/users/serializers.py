from rest_framework import serializers
from .models import User, DoctorProfile, PatientProfile, StaffProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# =============================
# User Serializer (Simplified)
# =============================
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# =============================
# Doctor Profile Serializer
# =============================
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        # fields = '__all__'
        exclude = ['user']


# =============================
# Patient Profile Serializer
# =============================
class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'
        read_only_fields = ['user']


# =============================
# Staff Profile Serializer
# =============================
class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        # fields = '__all__'
        exclude = ['user']


# =============================
# Custom JWT Token Serializer
# =============================
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom data to the token
        token['username'] = user.username
        token['role'] = user.role
        token['email'] = user.email
        token['is_verified'] = user.is_verified

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Prevent manual admin login via API
        if user.role == 'admin':
            raise serializers.ValidationError("You cannot login as admin via API.")

        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'is_verified': user.is_verified
        }

        return data
