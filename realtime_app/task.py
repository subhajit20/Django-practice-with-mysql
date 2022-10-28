from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import time

@shared_task(bind=True)
def sending_emails(self,email):
    time.sleep(5)
    subject = 'welcome to GFG world'
    message = 'Hi  thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list,fail_silently=False)
    return None