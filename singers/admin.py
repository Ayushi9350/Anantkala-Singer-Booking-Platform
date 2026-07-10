from django.contrib import admin
from .models import Singer, Genre, SingerGallery, ContactMessage, GalleryVideo 


class SingerGalleryInline(admin.TabularInline):
    model = SingerGallery
    extra = 3
    fields = ('image', 'caption')

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'price_per_event', 'experience_years', 'is_available', 'featured', 'is_approved')
    list_filter = ('genre', 'is_available', 'featured', 'is_approved')
    search_fields = ('name', 'bio')
    list_editable = ('is_available', 'featured', 'is_approved')
    inlines = [SingerGalleryInline]

    fieldsets = (
       ('Account', {
            'fields': ('user',)
        }),

       ('Basic Info', {
            'fields': ('name', 'photo', 'bio', 'genre', 'experience_years')
        }),

        ('Pricing', {
            'fields': ('price_per_event',)
        }),

        ('Contact', {
            'fields': ('contact_email', 'contact_phone', 'instagram', 'youtube')
        }),

        ('Status', {
            'fields': ('is_available', 'featured', 'is_approved')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SingerGallery)
class SingerGalleryAdmin(admin.ModelAdmin):
    list_display = ('singer', 'caption')
    list_filter = ('singer',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)

@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ('title',)