import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from news.models import Post, Category

logger = logging.getLogger(__name__)


def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(create__gte=last_week)

    subscribers = []
    for i in posts:                                                # Цикл по всем постам за прошедшую неделю
        for j in i.categories__category:                           # В каждом посте (через related_name='categories' в модели PostCategory)
            for k in get_object_or_404(Category, id=j).get_sub():  # получаем все объекты модели PostCategory, в которых есть данный пост
                subscribers.append(k.email)                        # Далее через двойное подчеркивание находим id категорий в этих объектах PostCategory
                                                                   # Находим категории по этим id, и через функцию модели Category (get_sub())
                                                                   # Находим наших подписчиков и добавляем их email в список подписчиков
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
            to=subscribe,
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second='*/10'),  #day_of_week="fri", hour="18", minute="00"
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),

            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

