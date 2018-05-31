from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.log_in, name='log_in'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^profile/$', views.profile, name='profile'),
]
