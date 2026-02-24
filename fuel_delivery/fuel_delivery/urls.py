from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path
from main import views  # if you are using views from main app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', include('main.urls')),  # if register is inside main.urls
    path('dashboard/', include('main.urls')),
    path('book/', include('main.urls')),
    path('track/<int:order_id>/', include('main.urls')),

    # Redirect root URL to dashboard
    path('', lambda request: redirect('dashboard')),  
]