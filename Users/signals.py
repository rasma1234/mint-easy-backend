
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=User)
def send_password_reset_email(sender, instance, **kwargs):
    if kwargs.get('created', False):  # Check if a new user is created
        # Your logic to generate reset URL and get username
        password_reset_url = 'your-reset-url'
        username = instance.username

        context = {'password_reset_url': password_reset_url, 'username': username}
        email_content = render_to_string('account/email/base_message.txt', context)

        # Your logic to send the email
        send_mail('Subject', email_content, settings.DEFAULT_FROM_EMAIL, [instance.email])
