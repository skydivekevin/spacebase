from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book
    

def booklist(request):
    # return HttpResponse("You hit the booklist page")
    books = Book.objects.all().order_by('title')
    return render(request, 'booklist/booklist.html', {'books': books})



    
