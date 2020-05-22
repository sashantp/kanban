from django.urls import path
from board import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

