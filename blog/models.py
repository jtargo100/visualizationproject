from django.db import models


class Visuals(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=200)


    def __str__(self):
        return self.title
