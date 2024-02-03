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
        notify_new_post.delay(instance.pk)
