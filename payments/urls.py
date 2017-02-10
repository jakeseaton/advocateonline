from django.conf.urls import patterns, url

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^shopSubmit$', views.shopSubmit),
    url(r'^donate/$', views.donate),
    url(r'^sendDonation/$', views.sendDonation),
    url(r'^galadonation/$', views.galaDonation),
    url(r'^financialdonation/$', views.financialdonation),
    url(r'^stripeSubmit/$', views.stripeSubmit),
    url(r'^stripeSubmitShop/$', views.stripeSubmitShop),
    url(r'^subscribe$', views.subscribe)
)
