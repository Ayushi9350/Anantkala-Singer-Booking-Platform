from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Genres"

class Singer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="Singer Name")
    photo = models.ImageField(upload_to='singers/', verbose_name="Singer Photo")
    bio = models.TextField(verbose_name="Biography")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    experience_years = models.IntegerField(default=0, verbose_name="Years of Experience")
    price_per_event = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price Per Event (₹)")
    contact_email = models.EmailField(verbose_name="Contact Email")
    contact_phone = models.CharField(max_length=15, verbose_name="Contact Phone")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram Link")
    youtube = models.URLField(blank=True, null=True, verbose_name="YouTube Link")
    is_available = models.BooleanField(default=True, verbose_name="Available for Booking")
    is_available = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    featured = models.BooleanField(default=False, verbose_name="Featured Singer")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-featured', 'name']

class SingerGallery(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='singers/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.singer.name} - Gallery Image"
    
    class Meta:
        verbose_name_plural = "Singer Gallery"
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='bookings')
    event_date = models.DateField(verbose_name="Event Date")
    event_type = models.CharField(max_length=100, verbose_name="Event Type")
    message = models.TextField(blank=True, verbose_name="Message")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.singer.name} ({self.status})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SingerLike(models.Model):
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('singer', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.singer.name}"

class GalleryVideo(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='gallery_videos/')

    def __str__(self):
        return self.title