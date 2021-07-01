from django.urls import path
from . import views

app_name = 'NewsApp'
urlpatterns = [
    path('list', views.index, name='index'),
    path('tag/<str:tag>/', views.tag_list, name='tag_list'),
    path('<int:news_id>/', views.detail, name='detail'),
    path('stat', views.stat, name='stat'),
    path('create', views.create_news, name='create_news'),
]
