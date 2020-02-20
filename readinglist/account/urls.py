from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('userpage/', views.userpage, name='userpage'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('userpage/userrating/', views.userrating, name='userrating'),
    path('userpage/deleteuserfavorite/', views.deleteuserfavorite, name='deleteuserfavorite'),

]