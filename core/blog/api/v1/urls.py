from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "api-v1"

urlpatterns = [

    # path('post/', views.postList, name='post-list'),
    path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:id>/', views.postDetail, name='post-detail'),

]