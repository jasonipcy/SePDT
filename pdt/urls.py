from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^development/$', views.development_page, name='development_page'),
	url(r'^log/$', views.log_page, name='log_page'),
    url(r'^set_time/$', views.set_time, name='development_set_time'),
    url(r'^$', views.hello, name='hello'),
	# url(r'^login/', 'learn.views.login', name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^hello/$', views.hello, name='hello'), 
]
