from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from player.models import *
from player.dao  import teamDao, playerDao
from player.action import playerAction
import datetime


# Create your views here.
def index(request):
    context = {'team_list': teamDao.getTeams()}      
    return render(request, 'team/index.html', context)


def teamDetail(request, team_id):
    #team = get_object_or_404(Team, pk=team_id)
    team = teamDao.getTeamById(team_id)
    return render(request, 'team/team_detail.html', {'team': team})


def playerDetail(request, team_id, player_id):
    '''
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    '''
    team = teamDao.getTeamById(team_id)
    player = playerDao.getPlayerById(player_id)
    '''
    mark_date = player.last_mark_time.date()
    mark_time = str(player.last_mark_time.time())[:5]
    '''
    player_set = team.player_set.all()
    #print(player_set,'player set')
    return render(request, 'team/player.html', {'player': player,
                                                'team': team,
                                                'team_list': teamDao.getTeams(),
                                                'player_set': player_set,
                                               })    

def mark(request, team_id, player_id):
    player = playerDao.getPlayerById(player_id)
    new_mark = float(request.POST['mark_input'])

    mark_time = playerAction.setNewMark(player, new_mark)
    #return render(request, 'team/player.html', {'player': player,'team':team})  
    return HttpResponseRedirect(reverse('team:player', args=(team_id, player_id)))


