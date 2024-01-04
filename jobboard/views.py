# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import JobListing, Application


# def job_search(request):
#     query = request.GET.get('q')
#     location = request.GET.get('location')
#     if query:
#         jobs = JobListing.objects.filter(title__icontains=query)
#         if location:
#             jobs = jobs.filter(location__icontains=location)
#     else:
#         jobs = JobListing.objects.all()
#     return render(request, 'job_search.html', {'jobs': jobs})


def job_search(request):
    query = request.GET.get('q')
    location = request.GET.get('location')
    jobs = JobListing.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:  # Add this condition for location filtering
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'job_search.html', {'jobs': jobs})


def apply_job(request, job_id):
    job = JobListing.objects.get(id=job_id)
    if request.method == 'POST':
        # handle application submission
        Application.objects.create(job_listing=job, job_seeker=request.user.jobseeker, status='Applied')
        # send notification to employer
        # implement notification logic
        return redirect('job_search')
    return render(request, 'apply_job.html', {'job': job})


def job_details(request, job_id):
    # Retrieve the job listing based on the job_id
    job = get_object_or_404(JobListing, id=job_id)

    # Render the job details template with the job listing data
    return render(request, 'job_details.html', {'job': job})
