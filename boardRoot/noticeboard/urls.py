from django.urls import path
from . import views  # noticeboard의 views를 임포트한다

app_name = 'noticeboard' #일종의 도메인 생성
urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write_article, name='write_article'),
    #write라는 주소로 들어와 views밑에 write함수를 호출
    #path('add', views.add_article, name='add_article'),
]