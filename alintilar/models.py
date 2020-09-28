from django.db import models

# Create your models here.

class alinti(models.Model):
    cumle = models.CharField(max_length=500)
    yazici = models.CharField(max_length=500)
    resim = models.ImageField(default = 'N.Tesla.jpg' )
    def __str__(self):
        return self.cumle
