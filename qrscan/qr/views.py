from .models import Qr
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    qr = Qr.objects.all().first()
    context = {"qr":qr}
    return render(request, "index.html", context)


def logging(request):
    return render(request,"home.html")

def usuarios(request):
    return render(request,"registration/login.html")
