from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('allauth.urls')),

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    path('', include('singers.urls')),
    path('booking/', include('booking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Custom admin site header
admin.site.site_header = "🎵 Anantkala Admin Panel"
admin.site.site_title = "Anantkala Singer Management"
admin.site.index_title = "Welcome to Anantkala Dashboard"
