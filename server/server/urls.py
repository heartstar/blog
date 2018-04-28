
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # **url(r'^$', TemplateView.as_view(template_name="index.html")),**
    url(r'^blog/', include('blog.urls')),
]
