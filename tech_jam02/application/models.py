from django.db import models

# Create your models here.
#ここに問題を入れる

class Question(models.Model):

    TPO_CHOICE = [
        ("communication", "会話・コミュニケーション編"),
        ("cleanliness", "清潔感・身だしなみ編"),
        ("date", "デート・距離感編"),
        ("mental", "メンタル・余裕編"),
    ]
    category = models.CharField(
    max_length=50,
    choices=TPO_CHOICE
    )
    text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Q{self.order}.{self.text}"
    
class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    text = models.TextField()
    points = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.question} - {self.order}({self.points}点)"