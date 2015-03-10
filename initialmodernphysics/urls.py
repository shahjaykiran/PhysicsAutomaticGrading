from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'initialmodernphysics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^physics/', include('physics.urls', namespace="physics")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', views.serve)
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
