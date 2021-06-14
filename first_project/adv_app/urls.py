from django.urls import path
from adv_app import views

app_name = "adv_app"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view()),
]
