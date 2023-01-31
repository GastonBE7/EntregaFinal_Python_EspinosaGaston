from django.db import models

class Band(models.Model):
    name_band =models.CharField(max_length=100)
    members=models.IntegerField()
    musical_genre=models.CharField(max_length=100)
    ig=models.CharField(max_length=100)
    contact=models.IntegerField()
    

    def __str__(self):
        return self.name_band

class Turn(Band):

    CHOICES = (
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    )

    own_instruments=models.BooleanField(default=True)
    turn_assigned =models.CharField(choices=CHOICES, max_length=6)
    creation_time =models.DateTimeField(auto_now_add=True)
