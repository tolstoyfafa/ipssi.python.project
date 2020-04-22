from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ad
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    template = loader.get_template('hello.html')
    context = {
        'greeting': "hello world"
    }
    return HttpResponse(template.render(context, request))


def getAllAds(request):
    template = loader.get_template('adds.html')
    context = {
        'ads': Ad.objects.all()
    }
    return HttpResponse(template.render(context, request))


def demand(request):
    template = loader.get_template('demands.html')
    context = {
        'demands': Ad.objects.filter(type='demand')
    }
    return HttpResponse(template.render(context, request))


def supply(request):
    template = loader.get_template('supplies.html')
    context = {
        'supplies': Ad.objects.filter(type='supply')
    }
    return HttpResponse(template.render(context, request))


def details(request, ad_id):
    template = loader.get_template('detail.html')
    my_id = int(ad_id)
    try:
        context = {
            'ad': Ad.objects.get(pk=my_id)
        }
    except Ad.DoesNotExist:
        raise Http404("No AD matches the given query.")
    return HttpResponse(template.render(context, request))
