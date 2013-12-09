from django.conf.urls import patterns, url

from note import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/autor/$', views.AutorView.as_view(), name='autor'),
)
