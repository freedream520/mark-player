from django.conf.urls import patterns, url

from player import views

urlpatterns = patterns('',
  
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
   
    url(r'^(?P<team_id>\d+)/$', views.teamDetail, name='teamDetail'),
    #url(r'^(?P<class_id>\d+)/$', views.ClassroomDetailView.as_view(), name='classroom'),
    url(r'^(?P<team_id>\d+)/(?P<player_id>\d+)$', views.playerDetail, name='player'),
   # url(r'^(?P<class_id>\d+)/(?P<student_id>\d+)/$', views.playDetail, name='student'),
    
    #url(r'^(?P<class_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<team_id>\d+)/(?P<player_id>\d+)/mark/$', views.mark, name='mark'),
)