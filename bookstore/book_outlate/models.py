from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Adress(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street} , {self.postal_code} , {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries" 

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    adress = models.OneToOneField(Adress , on_delete=models.CASCADE , null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
    def book_titles(self):
        return ", ".join([book.title for book in self.books.all()])
    book_titles.short_description = "Book Title"


class Book(models.Model):
    title = models.CharField(unique=True,max_length=50)
    ratting = models.FloatField(
        validators=[MinValueValidator(0),MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE , null=True , related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False , blank=True,
                             db_index=True)
    published_country = models.ManyToManyField(Country,null=False,related_name="books")

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} ({self.ratting}) -> {self.author} & Bestselling = {self.is_bestselling}"