import time

from celery import shared_task
import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Post
from django.conf import settings


@shared_task
def notify_new_post(pk):
    new_post = Post.objects.get(pk=pk)
    categories = new_post.category.all()
    subscribers = []

    for category in categories:
        for user in category.get_sub():
            subscribers.append(user)

    subscribers = set(subscribers)

    for subscribe in subscribers:

        html_content = render_to_string(
            'new_post_notify.html',
            {
                'user': subscribe,
                'text': new_post.preview,
                'link': f'{settings.SITE_URL}{new_post.get_absolute_url()}'
            }
        )

        msg = EmailMultiAlternatives(
            subject=new_post.title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscribe.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

@shared_task
def weekly_send_email_task():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(create__gte=last_week)

    subscribers = []
    for i in posts:
        for j in i.category.all():
            for k in j.get_sub():
                subscribers.append(k.email)

    subscribers = set(subscribers)

    html_content = render_to_string(
        'posts_for_week.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    for subscribe in subscribers:
        msg = EmailMultiAlternatives(
            subject='Статьи за неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscribe],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()