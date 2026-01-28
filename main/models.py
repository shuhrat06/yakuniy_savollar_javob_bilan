from django.db import models

class Savol(models.Model):
    savol=models.TextField()

    class Meta:
        verbose_name_plural="Savollar"
    
    def __str__(self):
        return self.savol


