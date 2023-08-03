from django.shortcuts import render, HttpResponse, redirect
from akash.models import Course, Video


def checkout(request, slug):
    course = Course.objects.get(slug=slug)

    if not request.session.get('name', False):
        return redirect('LoginPage')

    context = {'course': course}
    return render(request, 'course/checkout.html', context=context)
