from formsapp.forms import NewUserForm
from django.shortcuts import render
from formsapp import forms
from formsapp.models import User

# Create your views here.


def index(request):
    return render(request, "formsapp/index.html")


def basic_form_view(request):
    form = forms.BasicForm()
    if request.method == "POST":
        form = forms.BasicForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("NAME: " + form.cleaned_data["name"])
            print("EMAIL: " + form.cleaned_data["email"])
            print("TEXT: " + form.cleaned_data["text"])

    return render(request, "formsapp/form_page.html", {"form": form})


def sign_up(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR - FORM INVALID")
    return render(request, "formsapp/sign_up.html", {"form": form})


def show_users(request):
    user_list = User.objects.order_by("fname")
    user_dict = {"users": user_list}
    return render(request, "formsapp/show_users.html", user_dict)
