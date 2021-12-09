from django.db import models


# Create your models here.
class Trainerinfo(models.Model):
    trainer_name = models.CharField(max_length=20)
    hometown = models.CharField(max_length=20)

    def __str__(self):
        return (self.trainer_name)


class Pokemon(models.Model):#changes Customers to Pokemon
    poke_name = models.CharField(max_length=30)
    poke_type = models.CharField(max_length=30)
    

    
    def __str__(self):
        return (self.poke_name)

