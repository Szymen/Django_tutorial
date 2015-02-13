from django.contrib import admin

# Register your models here.
from django.utils import timezone
from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline): # .TabularInline mowi w jaki sposob jest to sformatowane
    model= Choice #co (jaki obiekt) bedzie reprezentowane linia po lini
    extra = 2  #ile dodatkowych jest dodawanych, pustych


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets=[
        ("Pytanie !",              {'fields': ['question_text']}),
        ('Reszta info : ',{'fields': ['pub_date'],
                           'classes':['collapse']}), #pozwala na zwijanie opcji

    ]
    inlines = [ChoiceInline] # dodaje w liniach mozliwe odpowiedzi itd.
    list_display = ('question_text', 'pub_date' ,'was_published_recently') # w ogolnym podladzie ustala co jest wyswietlane
    list_filter = ['pub_date','question_text']  # dodaje mozliwosc filtrowania danych, pobiera tablice dozwolonych wyborow
    search_fields = ['question_text'] #dodaje wyszukanie na gorze

admin.site.register(Question, QuestionAdmin) # tworzy panel admina
#admin.site.register(Choice) # panel admina dla "Choice"
