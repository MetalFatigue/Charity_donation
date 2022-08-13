from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name


class Institution(models.Model):
    CHOICES = (
        ('0', "fundacja"),
        ('1', "organizacja pozarządowa"),
        ('2', "zbiórka lokalna"),
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=CHOICES, default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['type', 'name']
        verbose_name = 'Instytucja'
        verbose_name_plural = 'Instytucje'

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False,)
    city = models.CharField(max_length=30, null=False, blank=False)
    zip_code = models.CharField(max_length=6, null=False, blank=False)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=220, blank=True)
    user = models.ForeignKey(User, null=True, default=0, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Darowizna'
        verbose_name_plural = 'Darowizny'
