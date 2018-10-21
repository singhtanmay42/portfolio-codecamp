from django.db import models

# Create your models here.
class blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add= False)
     