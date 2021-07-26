from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def exercise1(request):
    template = loader.get_template("exercise1.html")
    name = request.GET.get('name', '하재연')
    context = {'result': name}
    return HttpResponse(template.render(context, request))


def exercise2(request):
    type = request.GET.get('type')
    if not type:
        context = {'type': None, 'msg': "type = memberlist 또는 type = number 로 쿼리를 전달하세요"}
    else:
        context = {'type': type, 'memberlist': ['둘리', '또치', '도우너', '희동이'], 'number': len(['둘리', '또치', '도우너', '희동이'])}
    return render(request, 'exercise2.html', context)
