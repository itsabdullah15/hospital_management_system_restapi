# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import User, DoctorProfile, PatientProfile, StaffProfile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     # Ensure that profiles are created only when a new User instance is created
#     if created:
#         if instance.role == 'doctor':
#             DoctorProfile.objects.create(user=instance)
#         elif instance.role == 'patient':
#             PatientProfile.objects.create(user=instance)
#         elif instance.role == 'staff':
#             StaffProfile.objects.create(user=instance)
#         # If the user is an admin, you can decide if you want to create a profile or leave it as is.
#         # You might not need a profile for the admin user unless you want to store additional admin-specific data.
#         elif instance.role == 'admin':
#             # Admins typically don't need a profile, so you can skip this, or create a specific profile if necessary.
#             pass  
