from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()

    def __str__(self):
        return f"{self.client_name} - {self.car}"