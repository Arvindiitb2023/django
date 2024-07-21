from django.contrib import admin
from django.urls import path, include
from users import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('home', user_views.home, name='home'),
path('profile', user_views.profile, name='profile'),
    path('' ,user_views.navbar,name='navbar')
]