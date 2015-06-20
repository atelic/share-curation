from django.conf.urls import include, url
from django.contrib import admin

from crowd import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
