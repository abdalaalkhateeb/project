from django.db import models

# Create your models here.
class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hero/')
    
    def __str__(self):
        return self.title