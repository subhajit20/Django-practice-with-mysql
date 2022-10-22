from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task(bind=True)
def sending_emails(self):
    subject = 'welcome to GFG world'
    message = 'Hi  thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["subhajitstd07@gmail.com", ]
    flag = send_mail(subject, message, email_from, recipient_list)
    return flag