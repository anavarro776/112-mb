

# Create your models here.
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title= models.CharField (max_length=128)
    subtitle = models.CharField(max_length=256)
    body= models.TextField() 
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse ("post_detail", args=[self.id])

# Create your models here.
  
    