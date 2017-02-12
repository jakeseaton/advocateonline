from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

from rest_framework import routers, serializers, viewsets

from magazine import views

from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index),
    url(r'^home/$', TemplateView.as_view(template_name="base_new.html")),
    url(r'^issues$', views.issues),
    url(r'^about$', views.masthead),
    url(r'^issue/(?P<season>[a-zA-Z]+)-(?P<year>[\d]{4})/$', views.singleissue),
    url(r'^submit$', views.submit),
    url(r'^contact$', views.contact),
    url(r'^alumni$', views.alumni),
    url(r"^fiction/$|^poetry/$|^art/$|^features/$|^columns/$|^notes/$", views.sections),
    url(r'^advertise$', views.advertise),
    url(r'^150th$', views.onefifty),
    url(r'^shop$', views.shop),
    url(r'^shop/(?P<id>\d+)$', views.shopItemView),
    url(r'^cart$', views.cart),
    url(r'^shop-admin$', views.shop_admin),
    url(r'^shop-upload$', views.shop_upload),
    url(r'^shop-delete$', views.shop_delete),
    url(r'^benefit$', views.gala),
    url(r'^financialaid$', views.financialaid),
    url(r'^comp$', views.comp),
    url(r'^article/(?P<id>[\d]+)/(?P<slug>[a-zA-Z\d_\-]+)/$', views.article),
    url(r'^content/(?P<id>[\d]+)/$', views.content_piece),
    url(r'^contributor/(?P<author_id>[\d]+)/(?P<name>.*)/$', views.contributor_page),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^search(?:/(?P<type_filter>[art|features|poetry|fiction]+))?/?$', views.FilterSearchView(), name='filter_search'),
    url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('payments.urls')),
    #http://stackoverflow.com/questions/901551/how-do-i-include-image-files-in-django-templates
    #http://stackoverflow.com/questions/19132123/name-settings-is-not-defined
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^anthology/', include('anthology.urls')),
    url(r'^api/', include('api.urls'))
)

