from django.urls import path, reverse_lazy,include
from .views import sign_up ,sign_in,logout_user,profile,edit_profile,change_pro_pic,user_info_change,pass_change

from django.contrib.auth import views as auth_views
app_name = 'App_login'

urlpatterns = [
    path('signup/',sign_up,name='sign_up'),
    path('login/',sign_in,name='sign_in'),
    path('logout/',logout_user,name='logout'),
    path('profile/',profile,name='profile'),
    path('change_profile/',edit_profile,name='edit_profile'),
    path('edit_profile_info/',user_info_change,name='edit_profile_info'),
    path('change_propic/',change_pro_pic,name='change_propic'),
    path('password/',pass_change,name='change_pass'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='App_login/registration/password_reset_form.html',
             subject_template_name='App_login/registration/password_reset_subject.txt',
             email_template_name='App_login/registration/password_reset_email.html',
             success_url='/account/password_reset_done/'
         ),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='App_login/registration/password_reset_done.html'
         ),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='App_login/registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='App_login/registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
    # password reset urls

    
   
   

