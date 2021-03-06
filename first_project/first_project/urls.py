"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from formsapp import views
from login_app import views
from django.contrib import admin
from django.urls import include, path

# from django.conf.urls import url


urlpatterns = [
    # url(r"^$", views.index, name="index"),
    path("", views.index, name="index"),
    path("formsapp/", include("formsapp.urls")),
    path("first_app/", include("first_app.urls")),
    path("basic_app/", include("basic_app.urls")),
    path("login_app/", include("login_app.urls")),
    path("adv_app/", include("adv_app.urls")),
    path("admin/", admin.site.urls),
]
