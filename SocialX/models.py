from django.db import models

# Create your models here.
class Profile_Pic(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/%y")
    def __str__(self):
        return self.name
