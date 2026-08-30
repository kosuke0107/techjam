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
         "question_count": question_count,
         "category": category,}
    )


def result(request):
    raw_points = request.GET.get("points", "0")
    category = request.GET.get("category", "")

    if raw_points.isdigit():
        points = int(raw_points)
    else:
        points = 0

    category_names = {
        "communication": "会話・コミュニケーション編",
        "cleanliness": "清潔感・身だしなみ編",
        "date": "デート・距離感編",
        "mental": "メンタル・余裕編",
    }

    category_name = category_names.get(category, "診断結果")

    return render(
        request,
        "application/result.html",
        {
            "points": points,
            "category": category,
            "category_name": category_name,
        }
    )

def question(request):
    return render(request, "application/question.html")

# Create your views here.
# ここに診断処理を書く
