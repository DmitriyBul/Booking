from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # post views
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),
]
