from django.shortcuts import render
from django.views import View

class IndexView(View):

    def get(self, request):
        contents = {
            'title': '我是顶',
            'book': {
                'a': 1,
                'b': 1,
                'c': 1,
                'd': 1,
                'e': 1,
            },
            'roo': [
                1, 2, 3, 4, 5, 6, 7, 8, 9
            ],
            'age': 18,
            'kong': [],
            'empty': '空的',
        }
        return render(request, 'index.html', context=contents)


def new(request):
    return render(request, 'new.html')


def tiyu(request):
    return render(request, 'tiyu.html')
