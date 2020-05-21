from django.db import models
from django.conf import settings


class Hotel(models.Model):
    CURRENCIES = (
        ('eur', '€'),
        ('czk', 'Kč'),
        ('usd', '$'),
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)
    image_description = models.CharField(max_length=100, null=True, blank=True)

    description = models.CharField(max_length=10000, null=True, blank=True)
    work_time = models.CharField(max_length=500, null=True, blank=True)

    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    parking = models.CharField(max_length=100, null=True, blank=True)
    price_description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True, choices=CURRENCIES)

    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)

    priority = models.IntegerField(null=True, blank=True)

    lat = models.CharField(max_length=10, null=True, blank=True)
    lng = models.CharField(max_length=10, null=True, blank=True)

    # Define model display name for Admin
    def __str__(self):
        return self.name


class HotelRegistration(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=10000, null=True, blank=True)
    processed = models.BooleanField(null=True, blank=True)

    # Define model display name for Admin
    def __str__(self):
        return self.email


class EmailSubscribe(models.Model):

    email = models.EmailField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    consent = models.BooleanField(null=True, blank=True)

    # Define model display name for Admin
    def __str__(self):
        return self.email
