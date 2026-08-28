from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import random


def index(request):
    return render(request, "application/index.html")


def ex(request, category=None):
    questions = Question.objects.prefetch_related("choice").order_by("order")

    if category:
        questions = Question.objects.filter(
            category=category
        ).order_by("order")
    else:
        questions = Question.objects.all().order_by(
            "category", "order"
        )

    question_count = questions.count()

    for question in questions:
        choices = list(question.choice.all())
        random.shuffle(choices)
        question.random_choices = choices

    return render(
        request,
        "application/ex.html",
        {"questions": questions,
         "question_count": question_count}
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
# ここに診断処理を書く
