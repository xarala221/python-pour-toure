from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .api import RegisterAPI, LoginAPI, UserAPI
from . import views
urlpatterns = [
    path("api/auth", include("knox.urls")),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path("login/", views.login_views, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_user, name="register"),
]
