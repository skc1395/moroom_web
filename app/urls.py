from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input/$', views.room_input, name='room_input'),
    url(r'^room/$', views.room_list, name='room_list'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^$', views.main, name='main'),
]
