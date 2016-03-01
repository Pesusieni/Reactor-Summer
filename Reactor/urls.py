from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Reactor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Front page
    url(r'^', include('photo.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
