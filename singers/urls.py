from django.urls import path
from . import views
from singers.views import gallery

urlpatterns = [
    path('', views.home, name='home'),
    path('singers/', views.singer_list, name='singer_list'),
    path('singers/<int:pk>/', views.singer_detail, name='singer_detail'),
    path('singers/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    ]