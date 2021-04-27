from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import ProductForm, RawProductForm
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors )
#     context = {
#         "form": my_form
#     }
#     return render(request,"product/product_create.html",context )


# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {
        
#     }
#     return render(request,"product/product_create.html",context )

def product_details_view(request, id):
    
    obj = get_object_or_404(Product, id = id)
    obj = Product.objects.get(id = id)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request,"product/product_details.html",context )

def product_list_view(request):
    queryset = Product.objects.all()
    # for i in queryset:
    #     print(i.id)
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)

def product_delete_view(request, my_id):

    obj = get_object_or_404(Product, id = my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request,"product/product_delete.html",context )

def username_view(request):
    #form = LoginForm()
    context = {
        #'form': form
    }
    return render(request, "product/login.html",context)

def product_create_view(request):
    initial_data = {
        'title': "my awsome title"
    }
    obj = Product.objects.get(id = 15)
    form = ProductForm(request.POST or None, )
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request,"product/product_create.html",context )

def logout_request(request):
     logout(request)
     messages.info(request, "Logged  out successfully")
   # return redirect('../product')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password= password)
            if user is not None:
                login(request, user)
                messages.info(request ,f"You are logged in as {username}") 
                return redirect("./details/")
            else:
                messages.error(request, "Invalid username or password")

    else:
        messages.error(request, "Invalid username or password")
        return redirect("../login")
    form = AuthenticationForm
    return render(request, "product/login.html", {'form': form})




# def render_initial_data(request):
    
#     form = RawProductForm(request.POST or None , initial = initial_data)
#     context = {
#         'form': form
#     }
#     return render(request,"product/product_create.html",context )
