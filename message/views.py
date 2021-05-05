from django.shortcuts import render
from userprofile.models import Userprofile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    queryset = User.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'message/index.html', context)