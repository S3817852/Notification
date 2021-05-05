from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import AddJobForm, ApplicationForm
from .models import Job
from userprofile.models import Userprofile
from userprofile import views
from userprofile.models import ConversationMessage
from django.views import View
from django.views.generic import (
    DetailView
)

from notification.utilities import create_notification
class JobObjectMixin(object):
    model = Job
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
    
class UserObjectMixin(object):
    model_user = User
    def get_user(self, user_id):
        # id = self.kwargs.filter(id='id')
        user = None
        if user_id is not None:
            user = get_object_or_404(self.model_user, username=user_id)
        return user
    
    # def get_queryset(self):
    #     queryset = Userprofile.objects.filter(user='kimanh')
    #     return self.get_queryset()

def search(request):
    return render(request, 'job/search.html')

class UserListView(View):
    queryset = User.objects.all()
    template_name = 'job/job_detail.html'
    def get(self, request, id = None, *args, **kwargs):
        context = {"object_list": queryset}
        return render(request, self.template_name,context)

    def get_queryset(self):
        return self.queryset


# Job detail and add comments
class JobDetailView(JobObjectMixin,UserObjectMixin,View):
    template_name = 'job/job_detail.html'

    def get(self, request, id = None, *args, **kwargs):
        context = {'job': self.get_object()}
        return render(request, self.template_name,context)

    def post(self, request,id =None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['job'] =  obj
            # form = CourseModelForm(request.POST, instance=obj)
            if request.method == 'POST':
                content = request.POST.get('content')
                to_user = request.POST.get('to')
                sent_to_user = self.get_user(to_user)
                print(sent_to_user)
                # queryset = User.objects.filter('to_user')
                # print(queryset)
                if content:
                    conversationmessage = ConversationMessage.objects.create(job=obj, content=content, created_by=request.user)
                    create_notification(request, sent_to_user, 'message', extra_id=obj.id)

                    return redirect('job_detail', id=obj.id)
            # if form.is_valid():
            #     form.save()
            
            # context['form'] =  form
        return render(request, self.template_name,context)

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    queryset = User.objects.all()
    # sent_to_user = Userprofile.objects.filter('kimanh')
    # print(sent_to_user)
    # if request.user.userprofile.is_owner:
    #     job = get_object_or_404(Job, pk=job_id, job__created_by=request.user)
    # else:
    #     job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    if request.method == 'POST':
        content = request.POST.get('content')
        # to_user = request.POST.get('to')
            # answer = form.cleaned_data['value']
        
        
        if content:
            conversationmessage = ConversationMessage.objects.create(job=job, content=content, created_by=request.user)

            # create_notification(request, abc , 'message', extra_id=job.id)
            create_notification(request, job.created_by, 'message', extra_id=job.id)

            return redirect('job_detail', job_id=job_id)
    return render(request, 'job/job_detail.html', {'job': job, "object_list": queryset})

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)

        return redirect('dashboard')
    else:
         form = ApplicationForm()
    
    return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            create_notification(request, job.created_by, 'application', extra_id=job.id)
            
            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'job/edit_job.html', {'form': form, 'job': job})