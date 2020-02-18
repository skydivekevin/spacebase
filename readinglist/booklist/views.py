from django.shortcuts import render, redirect
from .models import Book, Userfavorite
from booklist.forms import Addbook, Adduserbook


def booklist(request):
    if request.method == 'GET':
      print('booklist get')
      context = {}
      context['username'] = request.user
      context['books'] = Book.objects.all().order_by('title')
      context['userid'] = request.user.id
      form = Addbook()
      addbookform = Adduserbook()
      addbookform.userid = request.user
      context['form'] = form
      context['addbookform'] = addbookform
      return render(request, 'booklist/booklist.html', context)
    if request.method == 'POST':
        print('booklist post')
        form = Addbook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            newbook = Book(title=title, author=author)
            newbook.save()
            return redirect('/list/')
    return redirect('/list/')

def usersbooklist(request):
    print('userbooklist')
    if request.method == 'POST':
      userid = request.userid
      bookid = request.bookid
      print(userid)
      print(bookid)
      entry = Userfavorite(user=userid, book=bookid,)
      entry.save()
    return redirect('/accounts/userpage/')




  





    
