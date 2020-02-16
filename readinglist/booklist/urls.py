from django.urls import path

from . import views

app_name = 'booklist'


urlpatterns = [
    path('', views.booklist),
    path('list/', views.booklist, name='list'),
    path('addbook/', views.addbook, name='addbook')
]