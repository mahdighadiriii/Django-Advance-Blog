from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('fbv-index', views.indexView,name="fbv-index"),
    
    path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
]