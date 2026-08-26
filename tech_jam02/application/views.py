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

def result(request):
    raw_points = request.GET.get("points", "0")

    if raw_points.isdigit():
        points = int(raw_points)
    else:
        points = 0

    return render(
        request,
        "application/result.html",
        {"points": points}
    )


# Create your views here.
#ここに診断処理を書く