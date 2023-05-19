from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django_app.settings import * 


def send_verification_email(registeruserdata):
    mail_subject = 'Interview Confirmation - Drone Open Innovation Challenges'
    email_template = 'email_template.html'
    from_email = EMAIL_HOST_USER
    message = render_to_string(email_template, {
        'registeruserdata': registeruserdata
    })
    to_email = registeruserdata.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()