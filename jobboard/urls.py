from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_search, name='job_search'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('apply/', views.apply_job, name='apply_job'),
    # Add more URL patterns as needed
]
