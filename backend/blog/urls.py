from django.urls import path
from .views import home, post_detail, create_post

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
]
