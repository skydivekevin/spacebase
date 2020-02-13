from django.urls import path

from . import views

urlpatterns = [
    path('', views.booklist),
    # path('list/', views.booklist, name='list')
]