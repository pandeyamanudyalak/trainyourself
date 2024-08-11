from django.db import models

# Create your models here.


class Enquiry(models.Model):
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email