from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    like = models.NullBooleanField()
    category = models.CharField(max_length=20)


    def like(self):

      #  self.like = None
        self.save()

    def __str__(self):
        return self.title

    def luke(self):
        self.like = True
        self.save()
