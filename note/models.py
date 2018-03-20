from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    category = models.CharField(max_length=20)
    like = models.BooleanField(False)


   # def like(self):

    #    self.like = True
     #   self.save()

    def __str__(self):
        return self.title

    def luke(self):
        if self.like == True:
            self.like = False
        else:
            self.like = True
        self.save()
