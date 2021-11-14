from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    col = models.CharField(max_length=10)


class New(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now)


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Article(models.Model):
    title = models.CharField(max_length=50, default='Default')
    body = models.TextField(default='Default')
    date = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=300)
    publication = models.ManyToManyField(Publication)
    pub_date = models.DateField(default=timezone.now)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    def shorten_text(self):
        return self.body[:100]

    class Meta:
        ordering = ('headline',)


class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Cafe(Place):
    serves_coffee = models.BooleanField(default=False)
    serves_tuna = models.BooleanField(default=False)


class ContactInfo(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=40)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    phone = models.CharField(max_length=40)


class Staff(ContactInfo):
    position = models.CharField(max_length=40)
