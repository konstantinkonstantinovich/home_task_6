from django.contrib import admin

from .models import Author, Choice, LogModel, MyPerson, Question, Quote


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
    polls_person = ['question_text']


class LogModelAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "timestamps"]
    search_fields = ["path", "method", "timestamps"]
    fields = ['path', 'method', 'timestamps']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote']
    search_fields = ['quote']
    fields = ['quote']


admin.site.register(Question, QuestionAdmin)
admin.site.register(LogModel, LogModelAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
