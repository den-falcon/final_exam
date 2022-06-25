from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import UserProfileView, RegistrationView, LoginUser

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile',),
    path('login/', LoginUser.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout',),
    path('registration/', RegistrationView.as_view(), name='registration',),
]
