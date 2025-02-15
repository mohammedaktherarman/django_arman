from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:pk>/', views.teachers2, name='teacher2'),
    path('students/', views.students, name='students'),
    path('students/<int:pk>/', views.students2, name='students2'),
    
]