from django.shortcuts import render

from djangoIntroduction.to_do_app.models import Task


# Create your views here.


def index(request):
    title_filter = request.GET.get('name_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/index.html', context)