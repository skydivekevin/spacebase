from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=40, null=False, default="untitled")
    author = models.CharField(max_length=40, default="no author listed")
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # popularity = models.IntegerField
    # booklists = models.ManyToManyField(Booklist)


    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)




# many to many book to user
  