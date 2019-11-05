from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path("login/", views.login_views, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_user, name="register"),
]
