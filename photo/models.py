from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name
