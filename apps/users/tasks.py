"""User async tasks."""

# Django
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Celery App
from config import celery_app

# Utilities
from apps.utilities import (
    get_email_by_user_pk,
    get_email_v_token,
)


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
