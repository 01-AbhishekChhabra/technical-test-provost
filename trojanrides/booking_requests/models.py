from django.db import models
from uuid import uuid4

class Booking_Requests(models.Model):
    
    rider_name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey('drivers.Drivers', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.rider_name



