from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:singer_id>/', views.book_singer, name='book_singer'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('singer/register/', views.singer_register, name='singer_register'),
    path('singer/login/', views.singer_login, name='singer_login'),
    path('singer/logout/', views.singer_logout, name='singer_logout'),
    path('singer/dashboard/', views.singer_dashboard, name='singer_dashboard'),
    path('singer/booking/<int:booking_id>/update/', views.update_booking_status, name='update_booking_status'),
    path('singer/profile/edit/', views.edit_singer_profile, name='edit_singer_profile'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
]

