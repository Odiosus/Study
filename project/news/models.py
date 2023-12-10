from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        overall_rating = 0
        for i in self.posts.all():
            overall_rating += (i.rating*3)
            for j in i.comments.all():
                overall_rating += j.rating
        for k in Comment.objects.filter(user = self.user.id):
            overall_rating += k.rating
        self.rating = overall_rating
        self.save()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class RatingMixin:

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Post(RatingMixin, models.Model):
    news = 'NW'
    article = 'AR'
    CONTENT_LIST = [
        (news, 'Новость'),
        (article, 'Статья'),
    ]
    type = models.CharField(max_length=2, choices=CONTENT_LIST)
    title = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ManyToManyField(Category, through='PostCategory')
    create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return f'{self.text[:123]} ... '

    def __str__(self):
        return f'{self.author} : {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Категория {self.category} к посту {self.post.title}'

    class Meta:
        verbose_name = 'КатегорииПостов'
        verbose_name_plural = 'КатегорииПостов'


class Comment(RatingMixin, models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Комментарий пользователя {self.user} к посту {self.post.title} (ID: {self.id})'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
