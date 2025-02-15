from django.urls import path
from . import views

urlpatterns = [
    path('formulari/', views.formulari, name='formulari'),
    path('inici/', views.inici, name='inici'),
]