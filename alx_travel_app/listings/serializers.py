from rest_framework import serializers
from .models import Listing, Booking
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ListingSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'owner', 'address', 'city', 'country',
                 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms', 'created_at']
        
    def validate_price_per_night(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price per night must be positive")
        return value

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    guest = UserSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source='listing', write_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_id', 'guest', 'check_in', 'check_out', 
                 'total_price', 'created_at']
        
    def validate(self, data):
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        return data