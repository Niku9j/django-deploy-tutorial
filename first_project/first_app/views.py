from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage

# from django.http import HttpResponse

# Create your views here.


def indexOld(request):
    # return HttpResponse("<strong>Hello World!!!</strong>")
    my_dict = {"insert_me": "Hello I am being injected from views.py"}
    return render(request, "first_app/index_old.html", context=my_dict)


def index(request):
    web_pages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": web_pages_list}
    return render(request, "first_app/index.html", context=date_dict)
