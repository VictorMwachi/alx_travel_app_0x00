from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random
from decimal import Decimal
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def add_arguments(self, parser):
        parser.add_argument('--listings', type=int, default=20, 
                          help='Number of listings to create')

    def handle(self, *args, **options):
        fake = Faker()
        num_listings = options['listings']
        
        # Create or get a test user
        user, _ = User.objects.get_or_create(
            username='testowner',
            defaults={
                'email': 'owner@test.com',
                'password': 'testpass123'
            }
        )

        self.stdout.write(self.style.SUCCESS(f'Starting to seed {num_listings} listings...'))

        for _ in range(num_listings):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                owner=user,
                address=fake.street_address(),
                city=fake.city(),
                country=fake.country(),
                price_per_night=Decimal(random.uniform(50, 500)).quantize(Decimal('0.01')),
                max_guests=random.randint(1, 10),
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 3)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_listings} listings'))