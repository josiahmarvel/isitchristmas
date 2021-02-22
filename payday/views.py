from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.



def index(request):

    now = datetime.datetime.now()
    
    return render(request, "payday/index.html", {
        "payday": now.day == 25
    })
