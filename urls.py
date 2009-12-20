from django.conf.urls.defaults import *
import os
_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^regex_renom/', include('id3tagger.regex_renom.urls')),
    # Example:
    # (r'^id3tagger/', include('id3tagger.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^(.*/)?(?P<path>.*\.css)$', 'django.views.static.serve', {'document_root': '%s/template/css/' % _ROOT_PATH}),
	(r'^(.*/)?(?P<path>.*\.(jpg|png|gif))$', 'django.views.static.serve', {'document_root': '%s/template/img/' % _ROOT_PATH}),
	(r'^.*$', 'id3tagger.views.what'),
)
