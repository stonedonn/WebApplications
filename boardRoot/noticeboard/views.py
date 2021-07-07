from django.shortcuts import render
from noticeboard.models import Notice
# Create your views here.

def index(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글
    article_list = Notice.objects.all().order_by('-writeDate')
    context = {'article_list': article_list} #앞에는 키값 뒤에는 value
    return render(request, 'noticeboard/index.html', context)
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌

def write_article(request):
    return render(request, 'noticeboard/writeArticle.html')
