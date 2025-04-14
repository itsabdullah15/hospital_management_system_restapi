from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, recipient_list):
    """
    Sends a simple email using Django's send_mail.
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False
    )

def calculate_discount(price, discount_percent):
    """
    Apply discount and return the final price.
    """
    return price - (price * discount_percent / 100)
