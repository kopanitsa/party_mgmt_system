# -*- coding: utf-8 -*-
from django import forms

class EventCreationForm(forms.Form):
    item_name = forms.CharField()
