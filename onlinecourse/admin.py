from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInLine(admin.StackedInline):
    model = Question


class ChoiceInLine(admin.StackedInline):
    model = Choice

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_question = ['question']
    list_grade = ['grade']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

admin.site.register(Instructor)
admin.site.register(Learner)
