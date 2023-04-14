from .models import Qr
from django.shortcuts import render
from qrscan.settings import BASE_DIR


def index(request):
    qr = Qr.objects.all().first()
    context = {"qr":qr}
    return render(request, "index.html", context)


def logging(request):
    return render(request,"home.html")

def usuarios(request):
    return render(request,"registration/login.html")
