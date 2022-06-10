from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from Users import views as user_views
from django.contrib.auth import views as auth_views


favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    re_path(r'^favicon\.ico$', favicon_view),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]
