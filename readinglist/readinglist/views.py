import csv, datetime
from django.shortcuts import render, HttpResponse
from django.db.models import Count, Avg
from booklist.models import Book, Userfavorite


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

def list_download(request):
    now = datetime.datetime.now()
    userid = request.user.id
    items = Userfavorite.objects.filter(user_id=userid)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="booklist {}.csv"'.format(str(now))
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['book title', 'rating', 'tracking ids'])

    for item in items:
        writer.writerow([item.book, item.rating, item.tracking])
    return response







    
