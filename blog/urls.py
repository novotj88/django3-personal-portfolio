from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # pokud da nekdo do adresy int, posli tento int pod nazvem blog_id do views.all_blog
]
