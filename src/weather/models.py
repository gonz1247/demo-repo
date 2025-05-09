from django.db import models

# Create your models here.

class City(models.Model):
    class Meta:
        verbose_name_plural = 'cities'


    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name




