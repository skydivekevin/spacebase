from django.contrib import admin
from .models import Booklist, Book, Review

admin.site.register(Booklist)
admin.site.register(Book)
admin.site.register(Review)
