from django.db import models

class Beverage(models.Model):

    CHOICES = (
        (410, 410),
        (473, 473),
        (710, 710),
    )

    picture = models.ImageField(upload_to='beverage_picture', null=True, )
    brand = models.CharField(max_length=50)
    size = models.IntegerField(choices=CHOICES, default=473)
    quantity = models.IntegerField()
    creation_time =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand
