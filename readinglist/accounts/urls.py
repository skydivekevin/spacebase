from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('userpage/', views.userpage, name='userpage'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    # path('password_reset/', ),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('userpage/userrating/', views.userrating, name='userrating'),
    path('userpage/deleteuserfavorite/', views.deleteuserfavorite, name='deleteuserfavorite'),

]