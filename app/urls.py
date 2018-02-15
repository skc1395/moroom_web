from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.room_list, name='room_list'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
]
