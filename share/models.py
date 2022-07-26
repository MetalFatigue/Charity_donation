from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Institution(models.Model):
    CHOICES = (
        (0, "fundacja"),
        (1, "organizacja pozarządowa"),
        (2, "zbiórka lokalna"),
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=CHOICES, default=0)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False, unique=True)
    city = models.CharField(max_length=30, null=False, blank=False)
    zip_code = models.CharField(max_length=6, null=False, blank=False)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=220, blank=True)
    user = models.ForeignKey(User, null=True, default=0, on_delete=models.CASCADE)

