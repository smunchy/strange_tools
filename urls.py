from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin auto discover apps
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^newproject/', include('newproject.foo.urls')),
    # this is used for pages outside of the admin.
    url(r'^$', 'epictools.views.epictools_index', name ='home'),
    # The ?P<slug> is the variable area
    # the [-\w] means that we will accept any - or w ( any weird character or underscore)
    url(r'^epicBlog/(?P<slug>[-\w]+)$', 'epictools.views.epicBlog', name ="epicBlog"),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # admin interface
     url(r'^admin/', include(admin.site.urls)),
)
