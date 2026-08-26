from django.urls import path
from.import views
urlpatterns = [
    path("",views.index, name='index'),
    path("ex/",views.ex, name="ex"),
    path("result/", views.result, name="result"),
]








#テスト