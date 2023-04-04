from django.shortcuts import render

from convert import query


def index(request):
    statement = request.GET.get('content')
    answer = ''
    if statement:
        answer = query(statement)
    context = {
        'answer': answer
    }
    return render(request, 'index.html', context)
