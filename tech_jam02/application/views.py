from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"application/index.html")

def ex(request):
    return render(request,"application/ex.html")
# Create your views here.
#ここに診断処理を書く