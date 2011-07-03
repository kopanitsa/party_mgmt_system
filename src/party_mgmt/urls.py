from django.conf.urls.defaults import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # create event
    (r'^event_mgmt/create_event', 'party_mgmt.party.views.create_event'),
    (r'^event_mgmt/(?P<event_num>\d+)/(?P<event_name>\w+)$', 'party_mgmt.party.views.edit_event'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

