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
    """get all ads of an author"""
    template = loader.get_template('ads/ads.html')
    context = {
        'ads': Ad.objects.all()
    }
    return HttpResponse(template.render(context, request))


def demand(request):
    """ads filter by demand"""
    template = loader.get_template('demands/demands.html')
    context = {
        'demands': Ad.objects.filter(type='demand')
    }
    return HttpResponse(template.render(context, request))


def supply(request):
    """ads filter by supply"""
    template = loader.get_template('supplies/supplies.html')
    context = {
        'supplies': Ad.objects.filter(type='supply')
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    """Details of an Ad"""
    template = loader.get_template('details/detail.html')
    my_id = int(id)
    try:
        context = {
            'ad': Ad.objects.get(pk=my_id)
        }
    except Ad.DoesNotExist:
        raise Http404("No AD matches the given query.")
    return HttpResponse(template.render(context, request))
