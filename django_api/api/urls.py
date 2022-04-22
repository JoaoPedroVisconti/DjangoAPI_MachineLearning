from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllCandidatures, name='api')
]
