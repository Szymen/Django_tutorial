import datetime
from django.db import models
from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

    was_published_recently.admin_order_field='pub_date'             #wg czego sortowac
    was_published_recently.boolean= True                            #powoduje ze wyswietla w zestawieniu znaczek zamiast "true"/"false"
    was_published_recently.short_decription= 'Published recently ?' #opis metody



class Choice(models.Model):
    question= models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes =models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
