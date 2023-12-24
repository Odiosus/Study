from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter, ChoiceFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Author, Category

class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
    )
    create = DateTimeFilter(
        field_name='create',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        label='Начиная с:',
    )
    type = ChoiceFilter(
        field_name='type',
        choices=Post.CONTENT_LIST,
        label='Тип',
        empty_label='Любой',
        )

    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Любой',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['iregex'],
            'rating': ['lt', 'gt'],
        }
