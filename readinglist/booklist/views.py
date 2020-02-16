from django.shortcuts import render, redirect
from .models import Book    

def booklist(request):
    # return HttpResponse("You hit the booklist page")
    context = {}
    context['username'] = request.user
    context['books'] = Book.objects.all().order_by('title')
    # books = Book.objects.all().order_by('title')
    return render(request, 'booklist/booklist.html', context)

def addbook(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # content = body['title']
    print('Content is: ', request.body)
    return redirect('/list')





    
