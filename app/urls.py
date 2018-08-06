from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^input/$', views.room_input, name='room_input'),
    # url(r'^input/data$', views.input_data, name='input_data'),
    url(r'^room/(?P<university>\w+)/$', views.room_list, name='room_list'),
    url(r'^room/(?P<university>\w+)/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^room/(?P<university>\w+)/new/$', views.room_new, name='room_new'),
    url(r'^$', views.main, name='main'),
    url(r'^room/(?P<university>\w+)/(?P<pk>\d+)/edit/$', views.room_edit, name='room_edit'),
    url(r'^room/(?P<university>\w+)/(?P<pk>\d+)/delete/$', views.room_delete, name='room_delete'),
    url(r'^room/(?P<university>\w+)/(?P<pk>\d+)/complete/$', views.room_complete, name='room_complete'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),

]
