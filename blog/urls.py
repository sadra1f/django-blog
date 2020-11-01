from django.urls import path

from blog import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('posts/', v.blog, name='blog'),
    path('post/', v.post, name='post')
]