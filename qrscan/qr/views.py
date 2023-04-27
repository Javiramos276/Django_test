from .models import Qr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QrForm

@login_required
def index(request):
    qr = Qr.objects.filter(usuario=request.user)
    context = {"qr":qr}
    return render(request,"index.html", context)

def logging(request):
    return render(request,"home.html")

def usuarios(request):
    return render(request,"registration/login.html")

@login_required
def qrnuevo(request):
    form = QrForm()
    if request.method == 'POST':
        form = QrForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) #commit= False lo que hace es decir "no guardes esto aun", vamos a aplicar una accion mas y luego si vamos a guardar el post
            instance.usuario = request.user #Aca lo que hacemos es pedir el USUARIO asociado al modelo del qr a traves del request que esta haciendo el usuario en el form
            instance.save()
            return redirect('/accounts/login/bienvenido/')
    return render(request,'qrnuevo.html', {'form':form})
