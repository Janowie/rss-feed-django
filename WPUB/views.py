from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from django.http import HttpRequest
from xml.dom import minidom
import datetime
import os


def get_articles(request):
    articles = []
    url = ""
    if request.POST:
        url = request.POST.get('url')
        response = requests.get(url)
        # tree = ElementTree.fromstring(response.content)
        xmldoc = minidom.parseString(response.content)
        # print(tree)
        for e in xmldoc.getElementsByTagName("item"):
            article = {
                "title": e.getElementsByTagName("title")[0].firstChild.data,
                "desc": e.getElementsByTagName("description")[0].firstChild.data,
                # "date": e.getElementsByTagName("pubDate")[0].firstChild.data, # "%a, %d %b %Y %H:%M:%S +0100"
                "date": e.getElementsByTagName("pubDate")[0].firstChild.data,  # "%a, %d %b %Y %H:%M:%S +0100"
                "link": e.getElementsByTagName("link")[0].firstChild.data,
                "img": e.getElementsByTagName("enclosure")[0].getAttribute("url")
            }
            articles.append(article)
        articles = sorted(articles, key=lambda x: datetime.datetime.strptime(x['date'], "%a, %d %b %Y %H:%M:%S %z"),
                          reverse=True)
    return articles, url


def base(request):
    articles, url = get_articles(request)
    return render(request, 'base.html', {"articles": articles, "url": url})


def test_render(request):
    articles, url = get_articles(request)
    return render_to_string('base.html', {"articles": articles, "url": url})
