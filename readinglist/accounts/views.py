from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from booklist.models import Userfavorite
from booklist.forms import Deletebook, UserCreationFormEmail

def signup_view(request):
    form = UserCreationFormEmail()
    if request.method == 'POST':
        form = UserCreationFormEmail(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user) 
        return redirect('accounts:userpage')
    else:
        form = UserCreationFormEmail()
        return render(request, 'accounts/signup.html', {'form':form})

@login_required()
def userpage(request):
    context = {}
    username = request.user
    userid = request.user.id
    context['username'] = username
    context['userid'] = userid
    context['deletebookform'] = Deletebook
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
        tracking = request.POST.get('tracking')
        user = request.user
        book = Userfavorite.objects.filter(user=user).filter(id=objid)[0]
        book.rating = rating
        book.tracking = tracking
        book.save()
        return redirect('accounts:userpage')

def deleteuserfavorite(request):
    if request.method == 'POST':
        rowid = request.POST.get('userfavoriteid')
        print("rowid is: ", rowid)
        record = Userfavorite.objects.get(id=rowid)
        record.delete()
        return redirect('accounts:userpage')