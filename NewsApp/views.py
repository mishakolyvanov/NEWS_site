from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from NewsApp.models import News

def index(request):
    all_news_list = News.objects.order_by('-pub_date')
    return render(request, 'list.html', {'all_news_list': all_news_list})

def detail(request, news_id):
    try:
        a = News.objects.get( id = news_id)
    except:
        raise Http404("Статья не найдена!")

    return render(request, 'detail.html', {'news': a})
# def index(request):
#     latest_news_list = News.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.news_title for q in latest_news_list])
#     return HttpResponse(output)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
