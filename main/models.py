from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    

