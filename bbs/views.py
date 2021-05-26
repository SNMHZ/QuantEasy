from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator

# Create your views here.
@login_required
def strategy(request):
    """
    전략 게시판 목록
    """
    articles = StrategyArticle.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(page, posts)
    return render(request, 'bbs/board.html', { 'articles':articles , 'posts':posts})

@login_required
def strategy_detail(request, _id):
    """
    전략 게시판 디테일
    """
    try:
        article = StrategyArticle.objects.get(id=_id)
    except:
        return redirect('/bbs/strategy/')

    return render(request, 'bbs/detail.html', {'feed':article})

@login_required
def strategy_new(request):
    """
    전략 게시판 디테일
    """

    return render(request, 'bbs/new.html')