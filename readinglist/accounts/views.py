from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from booklist.models import Book, Userfavorite
from django.http import HttpResponse

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)  
      return redirect('accounts:userpage')
  else:
    form = UserCreationForm()
  return render(request, 'accounts/signup.html', {'form':form})

@login_required()
def userpage(request):
  context = {}
  username = request.user
  userid = request.user.id
  context['username'] = username
  context['userid'] = userid
  booklist = []

  for book in Userfavorite.objects.filter(user_id=userid):
    booklist.append(book)
  context['booklist'] = booklist

  return render(request, 'accounts/userpage.html', context)

def loginpage(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('accounts:userpage')
  else:
    form = AuthenticationForm()
  return render(request, 'accounts/loginpage.html', {'form':form})

def logoutpage(request):
  if request.method == 'POST':
    logout(request)
    return redirect('accounts:login')

def userrating(request):
  if request.method == 'POST':
    rating = request.POST.get('rating')
    objid = request.POST.get('favoriteid')
    book = Userfavorite.objects.filter(id=objid)[0]
    book.rating = rating
    book.save()
    return redirect('accounts:userpage')

    


