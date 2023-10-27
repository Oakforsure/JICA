from django.urls import path
from . import views

urlpatterns = [
    path('', views.bio_test, name='bio_test'),
]
