from django.contrib import admin

# Register your models here.
from .models import BlogPost,BlogCategory
admin.site.register([BlogPost,BlogCategory])