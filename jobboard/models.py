# models.py

from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    # other fields like company description, location, etc.


class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,null=True)
    # other fields like requirements, location, etc.


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields like skills, experience, etc.


class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'),
                                                      ('Rejected', 'Rejected')])
