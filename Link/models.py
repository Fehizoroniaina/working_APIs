from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.template.defaultfilters import slugify


class Link(models.Model) :
    target_url = models.URLField(max_length =200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20,blank= True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE ,related_name="Link_Link")
    created_date =models.DateField(auto_now_add=True)
    active= models.BooleanField(default=True)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass

# Create your models here.
