from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def exercise1(request):
    template = loader.get_template("exercise1.html")
    name = request.GET.get('name', '하재연')
    context = {'result': name}
    return HttpResponse(template.render(context, request))
