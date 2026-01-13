from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.age})"

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
