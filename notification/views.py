from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification
from job.models import Job

@login_required
def notifications(request):
    # if Notification.created_by != Notification.to_user:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 0)
        extra_id = request.GET.get('extra_id', 0)
        job = Job.objects.all()

        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()

            if notification.notification_type == Notification.MESSAGE:
                return redirect('job_detail', id=notification.extra_id)
            elif notification.notification_type == Notification.APPLICATION:
                return redirect('job_detail', job_id=notification.extra_id)
            elif notification.notification_type == Notification.COMMENT:
                return redirect('job_detail', job_id=notification.extra_id)

        context = {
            'job_list': job
        }
    
   
    
        return render(request, 'notification/notifications.html', context)
