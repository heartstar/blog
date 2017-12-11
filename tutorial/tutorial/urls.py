#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', blog_view.Index),
    url(r'^detail/(?P<id>\d+)/$', blog_view.Detail, name="blog_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


