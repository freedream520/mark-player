from django.conf.urls import patterns, url

from player import views
from django.conf import settings


urlpatterns = patterns('',
  
    url(r'^$', views.index, name='index'),
    
   
    url(r'^(?P<team_id>\d+)/$', views.teamDetail, name='teamDetail'),
    
    url(r'^(?P<team_id>\d+)/(?P<player_id>\d+)$', views.playerDetail, name='player'),
   
    url(r'^(?P<team_id>\d+)/(?P<player_id>\d+)/mark/$', views.mark, name='mark'),
    
    
)