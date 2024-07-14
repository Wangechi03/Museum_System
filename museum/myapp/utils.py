# museum/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(to_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Thank you for booking with us. Here are your booking details:\n\n{booking_details}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    
    send_mail(subject, message, email_from, recipient_list)
