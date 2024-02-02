from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from .models import PostCategory
from .tasks import notify_new_post


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

        notify_new_post(instance.preview(), instance.title, subscribers, absolute_url)
