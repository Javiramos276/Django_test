from .models import Qr
from django.shortcuts import render


def home(request):
    qr = Qr.objects.all().filter(titulo = "Mi curriculum").first()
    context = {"qr":qr}
    return render(request, "index.html", context)
