from django.contrib import admin
from akash.models import *

# Register your models here.
# If you want to inside the details--------------


class TagAdmin(admin.TabularInline):
    model = Tag


class LearningAdmin(admin.TabularInline):
    model = Learning


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]


admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Registration)
admin.site.register(Payment)
admin.site.register(UserCourse)
admin.site.register(Profile)
