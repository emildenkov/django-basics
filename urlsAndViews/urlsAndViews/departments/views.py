from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def redirect_to_index(request):
    return redirect('index')


def redirect_to_github(request):
    return redirect('https://github.com/emildenkov')


def view_with_int_pk_snd_slug(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f'<h1>Department name is: {department.name} with slug {department.slug} '
                        f'and id {department.id}</h1>')


def view_with_pk(request, pk):

    department = get_object_or_404(Department, pk=pk)

    return HttpResponse(f'<h1>The department with id {department.id} has name {department.name}</h1>')


def view_with_slug(request, slug):

    department = get_object_or_404(Department, slug=slug)

    return HttpResponse(f'<h1>The department with slug {department.slug} has name {department.name}</h1>')
