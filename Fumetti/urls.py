from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("fumetto_detail/<int:fumetto_id>", views.fumetto_detail, name="fumetto_detail"),
]