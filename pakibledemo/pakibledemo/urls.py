from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.preview.views import DemoTemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pakibledemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', DemoTemplateView.as_view(), ),
)
