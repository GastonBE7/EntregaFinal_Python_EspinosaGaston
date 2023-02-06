from django.db import models

class Beverage(models.Model):

    CHOICES = (
        (410, 410),
        (473, 473),
        (710, 710),
    )

    brand = models.CharField(max_length=50, unique=True)
    size = models.IntegerField(choices=CHOICES, default=473)
    quantity = models.IntegerField()

    def __str__(self):
        return self.brand
