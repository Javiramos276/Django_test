from .models import Qr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QrForm

@login_required
def index(request):
    qr = Qr.objects.all().first()
    context = {"qr":qr}
    return render(request, "index.html", context)


def logging(request):
    return render(request,"home.html")

def usuarios(request):
    return render(request,"registration/login.html")

@login_required
def qrnuevo(request):
    form = QrForm()
    if request.method == 'POST':
        print(request.POST)
        form = QrForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        print(form.errors)
        print("Es un post")
    return render(request,'qrnuevo.html', {'form':form})

