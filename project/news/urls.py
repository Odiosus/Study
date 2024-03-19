from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Author', AuthorViewset)
router.register(r'Category', CategoryViewset)
router.register(r'Post', PostViewset)
router.register(r'PostCategory', PostCategoryViewset)
router.register(r'Comment', CommentViewset)
router.register(r'Subscriptions', SubscriptionsViewset)


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>/', PostDetail.as_view(), name='articles_detail'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', PostUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('upgrade/', upgrade_user, name='upgrade_user'),
    path('subscriptions/', subscription, name='subscriptions'),
    path('api/', include(router.urls), name='api'),
]


