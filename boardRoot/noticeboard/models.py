from django.db import models
from django.utils.timezone import now

#models.py에서 테이블을 만든다 클래스타입으로
class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    writeID = models.CharField(max_length=50)

    #해당 객체를 출력하면 title이 나오게 한다
    def __str__(self):
        return self.title
# Create your models here.
