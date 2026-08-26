from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return render(request,"application/index.html")

def ex(request):
    questions = Question.objects.prefetch_related("choices").order_by("order")

    return render(
        request,
        "application/ex.html",
        {"questions": questions}
    )
# Create your views here.
#ここに診断処理を書く