from django.shortcuts import render, get_object_or_404
from noticeboard.models import Notice
from django.http import HttpResponseRedirect
from django.urls import reverse #{%%} 템플릿언어를 파이썬에서 대체해서 쓸 수 있게 하는 기능
from django.utils import timezone
# Create your views here.
# 뷰는 웹(클라이언트) 요청을 받고, 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공하여
# 그 결과를 템플릿에 보내준다. 데이터는 가공하는 처리를 해야한다 싶으면 뷰에서 함수를
# 작성하면 된다.
def index(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글
    article_list = Notice.objects.all().order_by('-writeDate')
    context = {'article_list': article_list} #앞에는 키값 뒤에는 value
    return render(request, 'noticeboard/index.html', context)
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌

def write_article(request):
    return render(request, 'noticeboard/writeArticle.html')

def add_article(request):
    notice = Notice() #Notice 객체를 만들어주고
    notice.title = request.POST['title']
    notice.content = request.POST['content']
    notice.writeID = 'bit'
    notice.save() #데이터베이스에 저장
    return HttpResponseRedirect(reverse('noticeboard:index'))

def view_article(request, article_id):
    notice = get_object_or_404(Notice, pk=article_id)
    return render(request, 'noticeboard/detail.html', {'article':notice})

def update_article(request, article_id):
    #수정하려면 일단 가져와야함
    notice = Notice.objects.get(id=article_id)

    if request.method == 'POST':
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        #writeDate는 수정한 날짜로 가져와야함
        notice.writeDate = timezone.datetime.now()
        notice.save()
        return HttpResponseRedirect(reverse('noticeboard:view', args={article_id})) #매겨변수 전달
    else:
        render(request, 'noticeboard/detail.html', {'article': notice})

def delete_article(request, article_id):
    #삭제하려면 일단 가져와야함
    notice = Notice.objects.get(id=article_id)
    notice.delete()
    return HttpResponseRedirect(reverse('noticeboard:index')) #첫화면으로 넘겨줌

# url -> html -> views순

