from _typeshed import Self
from django.db import models


class Category(models.Model):
  category_name= models.CharField(max_length=50, unique=True)
  slug= models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length=500,blank=True)
  cat_image = models.ImageField(upload='photos/categories',blank=True)


  def __str__(self):
    return Self.category_name