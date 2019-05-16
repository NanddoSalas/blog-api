"""User async tasks."""

# Django
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

# Models
from apps.users.models import User

# Utilities
import jwt

# Celery App
from config import celery_app


def get_email_by_user_pk(pk):
    """Retrive User's email by the given pk."""
    return User.objects.get(pk=pk).email

def get_email_v_token(email):
    """Create and return a JWT of type 'email_v' by the given email."""
    data = {
        'type': 'email_v',
        'email': email,
    }
    token = jwt.encode(
        payload=data,
        key=settings.SECRET_KEY,
        algorithm='HS256'
    )
    return token.decode()


@celery_app.task
def send_email_confirmation(pk):
    """Handle the asyc confirmation email send."""
    email = get_email_by_user_pk(pk=pk)
    token = get_email_v_token(email=email)

    body = (
        '{}'.format(token)
    )

    mail = EmailMultiAlternatives(
        subject='Confirm your email',
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['{}'.format(email)]
    )

    status = mail.send()
    return status