import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def dashboard(request):
    context = {
        'posts': [
            {
                'title': 'I am really bored !',
                'username': 'kiwi',
                'content': '',
            },

            {
                'title': 'I have to do my homework',
                'username': 'kiwi',
                'content': 'I must do my coding exercises in order to get better and become a successful programmer',
            },

            {
                'title': 'Guz',
                'username': 'kiwi',
                'content': 'Ne znam ',
            },

        ]
    }

    return render(request, 'forum_app/dashboard.html', context)


