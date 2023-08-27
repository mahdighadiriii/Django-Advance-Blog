from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "blog"

urlpatterns = [
    # path('fbv-index', views.IndexView,name='fbv-index'),
    # path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
    path("api/v1/", include("blog.api.v1.urls")),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
]
