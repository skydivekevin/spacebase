from django.shortcuts import render
from booklist.models import Book, Userfavorite
from django.db.models import Count, Avg


def index(request):
    context = {}
    topbooks = []

    popular = Userfavorite.objects.values('book').annotate(count=Count('book')).order_by('-count')[:5]
    
    for book in popular:
        currentid = book['book']
        booktitle = Book.objects.filter(id=currentid).values('title')
        topbooks.append(booktitle[0])
        context['topbooks'] = topbooks
    
    highestrated = Book.objects.annotate(rating_average=Avg('favorite__rating')).order_by('-rating_average')[:5]
    context['highestrated'] = highestrated

    dateadded = Book.objects.values('title').annotate(count=Count('created')).order_by('-count')[:5]
    context['dateadded'] = dateadded
    return render(request, 'homepage.html', context)







    
