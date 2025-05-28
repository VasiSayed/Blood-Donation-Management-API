from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_donor = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    condition = models.TextField()
    required_amount = models.DecimalField(max_digits=10, decimal_places=2)
    received_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='patients/', null=True, blank=True)
    reports=models.FileField(upload_to='report/',blank=False,null=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.donor.username} donated ₹{self.amount} to {self.patient.name}"
