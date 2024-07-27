from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Criminal(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    full_name = models.CharField(max_length=301, blank=False)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        super(Criminal, self).save(*args, **kwargs)


class Crime(models.Model):
    criminal = models.ForeignKey(Criminal, models.CASCADE)
    committed = models.CharField(max_length=100)
    
    class Degree(models.TextChoices):
        FEL = ('FELONY', "Felony")
        MISD = ("MISDOM", "Misdomeanor")

    degree = models.CharField(max_length=6, choices=Degree.choices, default=Degree.MISD)

    class_s = models.PositiveSmallIntegerField()
