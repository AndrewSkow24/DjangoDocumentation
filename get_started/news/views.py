from django.shortcuts import render
from django.template.context_processors import request

from .models import Article

# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    print(a_list)
    context = {"year": year, "article_list": a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    content = {
        "year": year,
        "month": month,
        "article_list": a_list
    }
    return render(request, 'news/year_month_archive.html', content)

def article_detail(request, pk):
    article = Article.objects.filter(pk=pk)
    content = {
        "pk": pk,
        "article": article
    }
    return render(request, 'news/details.html', content)
