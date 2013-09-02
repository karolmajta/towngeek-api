# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


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
