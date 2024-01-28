from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from .models import PostCategory


def notify(preview, title, subscribers, absolute_url):

    for subscribe in subscribers:

        html_content = render_to_string(
            'new_post_notify.html',
            {
                'user': subscribe,
                'text': preview,
                'link': f'{settings.SITE_URL}{absolute_url}'
            }
        )

        msg = EmailMultiAlternatives(
            subject=title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscribe.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@receiver(m2m_changed, sender=PostCategory)
def new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        absolute_url = instance.get_absolute_url()
        categories = instance.category.all()
        subscribers = []

        for category in categories:
            for user in category.get_sub():
                subscribers.append(user)

        subscribers = set(subscribers)
        print(categories)

        notify(instance.preview(), instance.title, subscribers, absolute_url)
