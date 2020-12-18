from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email",required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class PropicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')