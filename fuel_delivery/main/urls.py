from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/', views.book_order, name='book_order'),
    path('track/<int:order_id>/', views.track_order, name='track_order'),
]