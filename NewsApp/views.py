from django.http import Http404
from django.shortcuts import render
from NewsApp.models import News


def index(request):
    all_news_list = News.objects.order_by('-pub_date')
    return render(request, 'list.html', {'all_news_list': all_news_list})


def detail(request, news_id):
    try:
        a = News.objects.get(id=news_id)
        a.views_count += 1
        a.save()
    except:
        raise Http404("Статья не найдена!")

    return render(request, 'detail.html', {'news': a})





