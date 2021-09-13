
from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_html/', views.test_html, name='test'),
    path('pdf/', views.test_htmltopdf, name='test pdf')
]