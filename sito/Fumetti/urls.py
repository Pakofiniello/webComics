from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("fumetto_detail/<int:fumetto_id>", views.fumetto_detail, name="fumetto_detail"),
    path("login/", views.login_view, name="login_view"),
    path("register/", views.register_view, name="register_view")
]