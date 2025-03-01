from django.db import models
from django.urls import reverse
# Create your models here.

class Forex(models.Model):

    title = models.CharField(max_length= 100)
    file_type = models.CharField(choices=[('book', 'book'),('video', 'video')],max_length=10)
    slug = models.SlugField(null=True)
    description = models.CharField(max_length= 2000) #to talk some about the course
    price = models.IntegerField(null=False,default=0)

    #description,image,made by
    stars = models.IntegerField()
    count = models.IntegerField(null=True ,default=0)

    def __str__(self):
        return self.title
    
    def get_abs_url(self):
        return reverse("core:detail-view", kwargs={"slug":self.slug}) #f"/detail/{self.slug}/"