
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
