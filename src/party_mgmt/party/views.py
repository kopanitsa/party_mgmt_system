# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from party_mgmt.party.models import EventForm, Event, PersonForm, Date, \
    Available, Person

def create_event(req):
    print("create_event")
    form = EventForm(req.POST or None)
    if form.is_valid():
        # save input data
        new_item = form.save()
        # split and save date
        dates_str = new_item.dates_str
        dates = dates_str.split(',')
        for d_str in dates:
            d = Date(date=d_str)
            d.save()
            new_item.dates.add(d)
        # split and save event id
        event_name_id = new_item.event_name.replace(' ','_').replace('　','_').replace('/','_').replace('?','_')
        event_name_id = event_name_id.replace(';','_').replace('；','_').replace('@','_').replace('＠','_').replace('=','_')
        event_name_id = event_name_id.replace(':','_').replace('：','_').replace('&','_').replace('＆','_').replace('＝','_')
        event_name_id = event_name_id.replace('+','_').replace('＋','_').replace(',','_').replace('?','_').replace('？','_')
        event_name_id = event_name_id.replace('&','_').replace('＄','_').replace('、','_').replace('.','_').replace('。','_')
        new_item.event_name_id = event_name_id
        new_item.save()

        return render_to_response('show_event.html',
                                  {'event': new_item})

    # pass form and render the "form" value on html.
    return render_to_response('create_event.html',
                              {'form': form})
    
def edit_event(req, event_num, event_name):
    print("edit_event")
    event = get_object_or_404(Event,id=event_num)
    form = PersonForm(req.POST or None)
    print("name_id:"+event.event_name_id)

    if form.is_valid():
        # Register Person
        if len(req.POST.getlist('register')) != 0:
            print("regitser person")
            new_person = form.save()
            av_inputs = req.POST.getlist('availables')
            for av_input in av_inputs:
                a = Available(available=av_input)
                a.save()
                new_person.availables.add(a)
            event.persons.add(new_person)
            return render_to_response('edit_event.html',
                                  {'event': event, 'form': form})
        # Edit Person
        elif len(req.POST.getlist('edit')) != 0:
            print("edit person")
            persons = Person.objects.filter(name=form.cleaned_data['name']).filter(event__event_name__exact=event_name)
            for p in persons:
                Available.objects.filter(person__id__exact=p.id).delete()
                av_inputs = req.POST.getlist('availables')
                for av_input in av_inputs:
                    a = Available(available=av_input)
                    a.save()
                    p.availables.add(a)
                p.comment = form.cleaned_data['comment']
                p.save()
        # Delete Person
        elif len(req.POST.getlist('delete')) != 0:
            print("delete person")
            person = Person.objects.filter(name=form.cleaned_data['name']).filter(event__event_name__exact=event_name)
            person.delete()
            
    return render_to_response('edit_event.html',
                              {'event': event, 'form': form})


