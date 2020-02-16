from django.shortcuts import render, redirect
from .models import Book   
from booklist.forms import AddBook


def booklist(request):
    if request.method == 'GET':
      context = {}
      context['username'] = request.user
      context['books'] = Book.objects.all().order_by('title')
      form = AddBook()
      context['form'] = form
      return render(request, 'booklist/booklist.html', context)
    if request.method == 'POST':
      form = AddBook(request.POST)
      if form.is_valid():
        title = form.cleaned_data['title']
        author = form.cleaned_data['author ']
        newbook = Book(title=title, author=author)
        newbook.save()
      return render(request, 'booklist/booklist.html', context)

# def addbook(request):
#     template_name = 'booklist/'
    
    
    
    
    
    # if request.method == 'POST':
    #   form 
    #   return redirect('/list')


  





    
