from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from words_counter import views

urlpatterns = [
    path('', views.count_words, name='words_counter'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]