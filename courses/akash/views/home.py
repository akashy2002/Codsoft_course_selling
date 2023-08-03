from django.shortcuts import render, HttpResponse
from akash.models.course import Course


def index(request):
    alldata = Course.objects.all()

    context = {'alldata': alldata}

    return render(request, 'course/home.html', context=context)
