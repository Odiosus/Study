from django_filters import (
    FilterSet,
    ModelMultipleChoiceFilter,
    DateTimeFilter,
    ChoiceFilter,
    ModelChoiceFilter,
    CharFilter
)
from django.forms import DateTimeInput
from .models import Post, Author, Category

class PostFilter(FilterSet):

    title = CharFilter(
        field_name='title',
        lookup_expr='iregex',
        label='Заголовок',
    )

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

    author = ModelChoiceFilter(              # Буду переписывать, так как авторов (так же как и категорий по сути..)
        field_name='author',                 # может быть огромное количество,
        queryset=Author.objects.all(),       # и список может сильно растянуться, лучше производить поиск
        label='Автор',                       # с использованием CharFilter
        empty_label='Любой',
    )





