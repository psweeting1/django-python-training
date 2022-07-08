from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # super.save will save to the database
    # Whenever save is called it will populate the slug column with the title is slug form
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
