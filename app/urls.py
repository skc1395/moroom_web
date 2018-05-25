from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^input/$', views.room_input, name='room_input'),
    url(r'^input/data$', views.input_data, name='input_data'),
    url(r'^room/$', views.room_list, name='room_list'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^room/new/$', views.room_new, name='room_new'),
    url(r'^$', views.main, name='main'),
    url(r'^room/(?P<pk>\d+)/edit/$', views.room_edit, name='room_edit'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),

]
