from django.urls import path
from . import views

app_name = 'booklist'


urlpatterns = [
    path('list/', views.booklist, name='booklist-list'),
    path('userlist/', views.userlist, name='usersbooklist'),
]