from django.urls import path
from courses import views as course_views
from django.contrib.auth.views import login, logout
from courses import forms

urlpatterns = [
    path('login/', login, {'template_name': 'accounts/login.html', 'authentication_form': forms.LoginForm}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('signup/', course_views.signup, name='signup'),
    path('', course_views.login_redirect, name='login_redirect')

]
