from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('add_comment/', views.add_comment, name='add_comment')
]
