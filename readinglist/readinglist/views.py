from django.shortcuts import render
from booklist.models import Book, Userfavorite
from django.http import HttpResponse
from django.db.models import Count


def index(request):
    context = {}

    # popular = Userfavorite.objects.annotate(c=Count('book')).order_by('-c')
    # print(popular[0].book)
    # print(popular[1].book)
    # print(popular[2].book)

    popular = Userfavorite.objects.values('book').annotate(count=Count('book')).order_by('-count')
    print(popular)
    topfive = []
    for book in popular:
      book = Book.objects.filter(id=book.book)
      topfive.append(book)


    # context['topfive'] = topfive
    # bookratinglist = {}
    # #for each book(book id) find sum and then average rating
    # # get all book id's
    # books = Book.objects.all()
    # context['books'] = books
    # for book in books:
    #   currentbook = book.id
    #   print('current book id is: ', currentbook)
    #   ratings = Userfavorite.objects.filter(book_id=currentbook)
    #   for rating in ratings:

      

      # ratings = []
      # ratings = Userfavorite.objects.filter(book=currentbook)
      # # ratingsum = sum(ratings)
      # print('sum is: ', sum(ratings.rating))

    




    return render(request, 'homepage.html', context)







    
