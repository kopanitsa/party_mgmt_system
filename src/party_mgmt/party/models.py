# -*- coding: utf-8 -*-
from django.db import models
import django.forms as forms

class Available(models.Model):
    # 1 as OK, 2 as unknown, 3 as NG
    available = models.CharField(u'Availables',max_length=256)
    
    def __unicode__(self):
        return self.available

    class Meta:
        db_table = 'available'

class Person(models.Model):
    name = models.CharField(u'Name',max_length=256)
    comment = models.CharField(u'Comment',max_length=256, blank=True)
    availables = models.ManyToManyField(Available)
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'person'

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['availables'] 

class Date(models.Model):
    date = models.CharField(u'Event ID',max_length=64)

class Event(models.Model):
    event_name = models.CharField(u'Event Name',max_length=256)
    dates_str = models.CharField(u'Dates',max_length=256)
    description = models.CharField(u"Description",max_length=1024)
    dates = models.ManyToManyField(Date)
    persons = models.ManyToManyField(Person)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'event'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['persons','dates'] 
