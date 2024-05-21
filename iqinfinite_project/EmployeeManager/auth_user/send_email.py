from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, message, EMAIL_HOST_USER, recipient_list):
   # Send PDF via email (you can use the email sending logic here)
   email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
   #email.attach(temp_pdf.name, temp_pdf.read(), 'application/pdf') -->Not needed here for now
   return email.send(fail_silently=False)