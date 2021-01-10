from django.contrib import admin

from .models import Choice, LogModel, MyPerson, Question


@admin.register(MyPerson)
class MyPersonModelAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name"]
    fields = ['email', 'first_name', 'last_name']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    searpolls_personch_fields = ['question_text']


class LogModelAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "timestamps"]
    search_fields = ["path", "method", "timestamps"]
    fields = ['path', 'method', 'timestamps']


admin.site.register(Question, QuestionAdmin)
admin.site.register(LogModel, LogModelAdmin)
