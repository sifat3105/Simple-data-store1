from django.db import models

# Create your models here.
class Human(models.Model):
    name= models.CharField(max_length=20)
    age= models.PositiveIntegerField()
    image= models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
