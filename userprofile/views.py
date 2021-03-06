from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from job.models import Job, Application
from .models import ConversationMessage
from notification.utilities import create_notification

@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

# @login_required
# def view_announcement(request, job_id):
#     if request.user.userprofile.is_owner:
#         job = get_object_or_404(Job, pk=job_id, job__created_by=request.user)
#     else:
#         job = get_object_or_404(Job, pk=job_id, created_by=request.user)

#     if request.method == 'POST':
#         content = request.POST.get('content')
#         if content:
#             conversationmessage = ConversationMessage.objects.create(job=job, content=content, created_by=request.user)

#             create_notification(request, job.created_by, 'message', extra_id=job.id)

#             return redirect('view_announcement', job_id=job_id)
#     return render(request, 'userprofile/view_announcement.html', {'userprofile': request.user.userprofile})


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_owner:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', aplication_id=application_id)
    
    return render(request, 'userprofile/view_application.html', {'application': application})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_job.html', {'job': job})