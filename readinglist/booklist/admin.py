from django.contrib import admin
from .models import Book, userfavorite

# admin.site.register(Booklist)
admin.site.register(Book)
admin.site.register(userfavorite)
# admin.site.register(Review)
