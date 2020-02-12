from django.db import models
from django.conf import settings

class Booklist(models.Model):
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=False,
    on_delete=models.CASCADE,
  )
  name = models.CharField(max_length=100, null=False)


class Book(models.Model):
    title = models.CharField(max_length=40, null=False, default="untitled")
    author = models.CharField(max_length=40, default="no author listed")
    booklists = models.ManyToManyField(Booklist)

class Review(models.Model):
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)





# class Ratings(models.Model):
#   book = models.ForeignKey(models.Book)






# class Book(models.Model):
#     book_title = models.CharField(max_length=200)
#     book_author = models.CharField(max_length=80)
#     acme_tracking = models.IntegerField()
#     # pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.book_title

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     books = models.ManyToManyField(Book)

  