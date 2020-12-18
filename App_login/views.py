from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.shortcuts import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm,UserProfileForm , PropicForm , UserProfileChange
from .models import UserProfile


# Create your views here.


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:sign_in'))

    return render(request,'App_login/signup.html',context={'form':form})

def sign_in(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_rent:Home'))
    return render(request,'App_login/login.html',context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_rent:Home'))


@login_required
def profile(request):
    return render(request,'App_login/profile.html',context={})



@login_required
def edit_profile(request):
    form= UserProfileForm()

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            change_form=form.save(commit=False)
            change_form.user = request.user
            change_form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request,'App_login/change_profile.html',context={'form':form})


@login_required
def change_pro_pic(request):
    form = PropicForm(instance=request.user.user_profile)

    if request.method =='POST':
        form = PropicForm(request.POST,request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    
    return render(request,'App_login/change_profile.html',context={'form':form})


@login_required
def user_info_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)

    if request.method == 'POST':
        form= UserProfileChange(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request,'App_login/change_profile.html',context={'form':form})



@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)

    if request.method =='POST':
        form= PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:sign_in'))

    return render(request,'App_login/change_profile.html',context={'form':form})
