# -*- coding: utf-8 -*-
import uuid

from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import get_user_model
User = get_user_model()


def send_email(sender, to, subject, template_name, context_kwargs):
    txt_path = 'commons/email/txt/{0}.txt'.format(template_name)
    txt_template = get_template(txt_path)
    html_path = 'commons/email/html/{0}.html'.format(template_name)
    html_template = get_template(html_path)
    context = Context(context_kwargs)
    text_content = txt_template.render(context)
    html_content = html_template.render(context)
    msg = EmailMultiAlternatives(subject, text_content, sender, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def deactivate_for_emails(emails=None):
    emails = [] if emails is None else emails
    for email in emails:
        matching_users = User.objects.filter(email=email).all()
        for user in matching_users:
            user.is_active = False
            email_username, email_domain = email.split(u'@')
            suffix = unicode(uuid.uuid4())
            new_username = (email_username + u'+' + suffix)[:100]
            new_email = '@'.join([new_username, email_domain])
            user.email = new_email
            user.save()
