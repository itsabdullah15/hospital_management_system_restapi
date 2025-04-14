from django.contrib import admin
from apps.users.models import User, DoctorProfile, PatientProfile, StaffProfile


#Register the User model with the admin interface
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_verified', 'phone_number', 'address')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_verified')
    ordering = ('username',)
    
# Register the DoctorProfile model
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'qualification', 'years_of_experience', 'consultation_fee', 'license_number')
    search_fields = ('user__username', 'specialization', 'license_number')
    list_filter = ('specialization',)
    ordering = ('user__username',)
    
# Register the PatientProfile model
@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'blood_group', 'height_cm', 'weight_kg')
    search_fields = ('user__username', 'emergency_contact_name')
    list_filter = ('gender', 'blood_group')
    ordering = ('user__username',)
    

# Register the StaffProfile model
@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation', 'shift', 'joining_date', 'salary')
    search_fields = ('user__username', 'department', 'designation')
    list_filter = ('shift', 'department')
    ordering = ('user__username',)