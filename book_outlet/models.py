from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(null=False, default="", db_index=True)
    published_countries = models.ManyToManyField(Country, )

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.rating} {self.author} {self.is_best_selling}"
