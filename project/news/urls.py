from django.urls import path
from .views import PostList, PostDetail, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view()),
    path('search/<int:pk>', PostDetail.as_view()),

]
