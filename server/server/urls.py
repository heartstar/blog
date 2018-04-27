
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from blog import views as blog_api

urlpatterns = [
    path('admin/', admin.site.urls),
    # **url(r'^$', TemplateView.as_view(template_name="index.html")),**
    url(r'^api', 'blog_api'),
]
