from django.db import models

class Band(models.Model):
    name_band =models.CharField(max_length=100)
    members=models.IntegerField()
    musical_genre=models.CharField(max_length=100)
    own_instruments=models.BooleanField()
    ig=models.CharField(max_length=100)
    contact=models.IntegerField()
    

    def __str__(self):
        return self.name_band
