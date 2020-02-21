from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Userfavorite
from booklist.forms import Addbook, Adduserbook, Deletebook
import csv, io


def booklist(request):
    if request.method == 'GET':
        context = {}
        context['username'] = request.user
        context['books'] = Book.objects.all().order_by('title')
        context['userid'] = request.user.id
        form = Addbook()
        addbookform = Adduserbook()
        addbookform.userid = request.user
        context['form'] = form
        context['addbookform'] = addbookform
        context['deletebookform'] = Deletebook
        return render(request, 'booklist/booklist.html', context)
    if request.method == 'POST':
        form = Addbook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            newbook = Book(title=title, author=author)
            newbook.save()
            return redirect('/list/')
    return redirect('/list/')

def userlist(request):
    if request.method == 'POST':
        form = Adduserbook(data=request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            bookid = form.cleaned_data['bookid']
            entry = Userfavorite(user_id=userid, book_id=bookid,)
            entry.save()
            return redirect('/accounts/userpage/')

# def list_download(request):
#     print('asfafakfjhdalkdfjshalkdfsjhalksfhdklasjhflaksjhdf')
#     userid = request.user.id
#     items = Userfavorite.objects.filter(user_id=userid)
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="booklist.csv"'
#     writer = csv.writer(response, delimiter=',')
#     writer.writerow(['book', 'rating', 'tracking'])

#     for item in items:
#         writer.writerow([item.book, item.rating, item.tracking])
#     return response
    









  





    
