from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.main),
    url(r'^(?P<category>archives|writing|art|multimedia)/$', views.main),

    url(r'^post/(?P<slug>[a-zA-Z\d_\-]+)/$', views.post),
    # url(r'^theme', 'blog.views.theme'),
    url(r'^tag/(?P<slug>[a-zA-Z\d_\-]+)/$', views.tag_page),
    url(r'^theme/(?P<theme_id>[\d]+)$', views.theme),
    url(r'^contributor/(?P<author_id>[\d]+)$', views.contributor_page),
    url(r'^about/$', TemplateView.as_view(template_name="blog_about.html")),
    url(r'^select2/', include('select2.urls')),
)