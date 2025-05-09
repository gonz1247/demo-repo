from django.db import models

# Create your models here.

class City(models.Model):
    class Meta:
        verbose_name_plural = 'cities'


    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def unique_city_name(self):
        city_names = City.objects.exclude(pk=self.pk).values_list('name', flat=True)
        new_city_name = self.name
        if new_city_name in city_names:
            return False
        else:
            return True


