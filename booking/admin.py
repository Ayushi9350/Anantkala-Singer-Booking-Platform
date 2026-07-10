from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'singer', 'event_name', 'event_date', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'event_date', 'singer')
    search_fields = ('user__username', 'singer__name', 'event_name')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Booking Info', {
            'fields': ('user', 'singer', 'status', 'total_amount')
        }),
        ('Event Details', {
            'fields': ('event_name', 'event_date', 'event_time', 'event_location', 'event_type', 'guests_count')
        }),
        ('Additional', {
            'fields': ('special_requests', 'created_at')
        }),
    )
