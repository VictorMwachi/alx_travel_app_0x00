from django.db import models

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings', db_column='property_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', db_column='user_id')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Booking'  # Matches SQL table name

    def __str__(self):
        return f"Booking {self.booking_id} for {self.property.name}"

class Listing(models.Model):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', db_column='host_id')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=255, null=False)
    pricepernight = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Property'  # Matches SQL table name

    def __str__(self):
        return self.name

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    property_id = models.ForeignKey(Listing)
    user_id = models.ForeignKey(User)
    rating = models.IntegerField()
    comment = models.CharField()

    class Meta:
        db_table = 'Review'
    
    def __str__(self):
        return f"Review {self.review_id} for {self.property.name}"