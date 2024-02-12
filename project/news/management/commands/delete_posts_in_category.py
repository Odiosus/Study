from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет все посты указанной категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        if Category.objects.filter(name=options['category']).exists():
            category = Category.objects.get(name=options['category'])
            answer = input(f'Do you really want to delete all posts from category {options["category"]}? yes/no   ')
            if answer != 'yes':
                self.stdout.write(self.style.ERROR('cancel'))
                return
            posts = Post.objects.filter(category=category)
            if posts:
                posts.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted all posts from category {options["category"]}'))
            else:
                self.stdout.write(self.style.ERROR(f'Could not find posts from category {options["category"]}'))
        else:
            self.stdout.write(self.style.ERROR(f'Could not find category {options["category"]}'))

