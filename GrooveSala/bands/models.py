from django.db import models

class Band(models.Model):
    logo=models.ImageField(upload_to='band_logo', null=True, blank=True)
    name_band =models.CharField(unique=True, max_length=100)
    members=models.IntegerField()
    musical_genre=models.CharField(max_length=100,  null=True, blank=True)
    ig=models.CharField(max_length=100, null=True, blank=True)
    own_instruments=models.BooleanField(null=True, blank=True)
    contact=models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.name_band

class Turn(Band):

    CHOICES = (
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    )

    turn_assigned =models.CharField(choices=CHOICES, max_length=6,  null=True, blank=True)
    creation_time =models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    flyer = models.ImageField(upload_to='eventos', null=True)
