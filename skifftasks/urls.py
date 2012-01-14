from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Tasks:
    (r'', include('tasks.urls')),

    # Frontend
    (r'', include('frontend.urls')),

    # sorl.thumbnail
    (r'^', include('sorl.thumbnail.urls')),

    # sentry
    (r'^sentry/', include('sentry.web.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^browserid/verify/', 'views.browserid_verify')
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

handler404 = 'frontend.views.handle404'
