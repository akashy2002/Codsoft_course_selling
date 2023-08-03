from django.shortcuts import render, HttpResponse, redirect
from akash.models import Course, Video
from akash.models import Registration


def coursePage(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number=serial_number, course=course)
    if ((request.session.get('name', False) is False) and (video.is_preview is False)):
        return redirect('SignupPage')

    context = {'slug': slug, 'course': course, 'video': video}
    return render(request, 'course/courses.html', context=context)
