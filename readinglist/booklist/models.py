from django.db import models
from django.conf import settings

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    title = models.CharField(max_length=40, null=False, default="untitled")
    author = models.CharField(max_length=40, default="no author listed")
    class Meta:
        unique_together = ('title', 'author',)

    def __str__(self):
        return self.title

class Userfavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="favorite")
    rating = models.IntegerField(blank=True, null=True)
    tracking = models.CharField(max_length=30, default="N/A")





  