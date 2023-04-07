from django.shortcuts import render

# Create your tests here.

def home(request):
    return render(request,"index.html")

