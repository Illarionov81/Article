from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import RegisterView, UserDetailView, UserPasswordChangeView, UserChangeView, AllUserView, UserDelete

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='create'),
    path('users/', AllUserView.as_view(), name='users'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='delete'),
    path('<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='password_change')
]
