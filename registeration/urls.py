# from django.urls import path, include
# from .api import RegisterAPI
# from knox import views as knox_views

# urlpatterns = [
#     path('api/auth', include('knox.urls')),
#     path('api/register', include('knox.urls'), RegisterAPI.as_view(), name="register")
# ]

# accounts/api/urls.py

from django.urls import path, include

from knox.views import LogoutView

from .api import UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]
