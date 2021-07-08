from django.urls import path
from . import views  # noticeboard의 views를 임포트한다
# URL은 view와 template을 이어주는 역할을 하고, 이 부분을 만들어 주는 작업을
# URLconf라고 한다.path()함수 이용
app_name = 'noticeboard' #일종의 도메인 생성
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write_article, name='write_article'),
    #write라는 주소로 들어와 views밑에 write함수를 호출
    path('add/', views.add_article, name='add_article'),
    path('<int:article_id>', views.view_article, name='view'), #조회 REST API
    path('update/<int:article_id>', views.update_article, name='update'), #업데이트
    path('delete/<int:article_id>', views.delete_article, name='delete'), #삭제
]