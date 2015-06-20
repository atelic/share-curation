from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shareCuration import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^homepage/$', views.homepage, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
