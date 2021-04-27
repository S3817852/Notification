from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import RegistrationForm


# Create your views here.
def index(request):
    return render(request, "infor/tenant_sidebar.html")

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "infor/register.html", {'form': form})




