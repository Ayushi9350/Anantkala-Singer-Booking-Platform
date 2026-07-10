from django.db import models
from django.contrib.auth.models import User
from singers.models import Singer

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200, verbose_name="Event Name")
    event_date = models.DateField(verbose_name="Event Date")
    event_time = models.TimeField(verbose_name="Event Time")
    event_location = models.CharField(max_length=300, verbose_name="Event Location")
    event_type = models.CharField(max_length=100, verbose_name="Type of Event")
    guests_count = models.IntegerField(verbose_name="Expected Guests")
    special_requests = models.TextField(blank=True, verbose_name="Special Requests")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.singer.name} - {self.event_date}"

    class Meta:
        ordering = ['-created_at']
