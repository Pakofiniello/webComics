from django.urls import path
from . import views
from . import api
urlpatterns = [
    path("", views.index, name = "index"),
    path("fumetto_detail/<int:fumetto_id>/", views.fumetto_detail, name="fumetto_detail"),
    path("login/", views.login_view, name="login_view"),
    path("register/", views.register_view, name="register_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("profile_page/<int:user_id>", views.profile_page_view, name = "profile_page_view"),
    path("fumetto_detail/<int:fumetto_id>/manga_completato/", views.manga_completato, name="manga_completato"),

    #API
    path("profile_page/<int:user_id>/profilo_api/", api.profilo_api, name = "profilo_api")
]