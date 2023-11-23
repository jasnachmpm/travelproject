from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='pics', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)
