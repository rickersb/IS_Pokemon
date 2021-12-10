from django.db import models

# Create your models here.
class PokemonInfo(models.Model):
    pokemon_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image_path = models.CharField(max_length=100)
    height = models.CharField(max_length=50)
    weight = models.FloatField()
    description = models.CharField(max_length=300, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_info'
    def __str__(self):
        return (self.name)


class PokemonType(models.Model):
    pokemon = models.OneToOneField(PokemonInfo, models.DO_NOTHING, primary_key=True)
    type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'pokemon_type'
        unique_together = (('pokemon', 'type'),)
    
    def __str__(self):
        return (str(self.pokemon) + ": " + self.type)