from django.urls import path
from . import views
app_name='article'

urlpatterns = [
    path('',views.article_list,name='article_list'),
    path('create/',views.article_create,name='article_create'),
    path('<slug:name>/',views.article_detail,name='detail')
]
