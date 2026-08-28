from django.urls import path
from.import views
urlpatterns = [
    path("",views.index, name='index'),
    path("ex/",views.ex, name="ex"),
    path("result/", views.result, name="result"),
    path("quiz/<str:category>/",views.ex, name="quiz"),
]








#テスト