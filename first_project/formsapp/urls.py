from django.urls import path
from formsapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.show_users, name="show_users"),
    path("signup/", views.sign_up, name="sign_up"),
    path("formpage/", views.basic_form_view, name="basic_form"),
]
