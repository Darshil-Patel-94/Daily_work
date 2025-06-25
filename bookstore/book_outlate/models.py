from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(unique=True,max_length=50)
    ratting = models.FloatField(
        validators=[MinValueValidator(0),MaxValueValidator(5)])
    author = models.CharField(null = True , max_length=50)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False , db_index=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} ({self.ratting}) -> {self.author} & Bestselling = {self.is_bestselling}"