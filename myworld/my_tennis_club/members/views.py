from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
# new import for logging in 
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
 
# # def testing(request):
# #     template = loader.get_template('template.html')
# #     context = {
# #       'fruits': ['Apple', 'Banana', 'Cherry'],   
# #     }
# #     return HttpResponse(template.render(context, request))   
# def testing(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('template.html')
#     context = {
#       'mymembers': mymembers,

#     }
#     return HttpResponse(template.render(context, request))

def testing(request):
    mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template('template.html')
    context = {
      'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))


# function for login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('members')
            else:
                messages.error(request, 'Your account is not active.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html',{})
    # else:
    #     return render(request, 'login.html',{})
    
    
   



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('members')  # Redirect to members page or home
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
  
def logout_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active:
                logout(request, user)
                return redirect('login')
    
    
        