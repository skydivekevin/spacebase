from django.db import models


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=80)
    acme_tracking = models.IntegerField()
    # pub_date = models.DateTimeField('date published')

class User(models.Model):
    username = models.CharField(max_length=30)



class UserBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()



