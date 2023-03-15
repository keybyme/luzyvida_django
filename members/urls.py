from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('register_user', views.register_user, name='register'),
    path('logout_user', views.logout_user, name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='members/change-password.html'), name='password_change'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='members/password_reset_done.html'), name='password_reset_done'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='members/password_reset.html'), name='reset_password'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='members/change-password.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='members/password_reset_complete.html'), name='password_reset_complete'), 
     

]
