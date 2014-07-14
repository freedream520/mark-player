
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from player.models import *
from player.dao.playerDao import *
from player.dao.teamDao import *
from player.action import playerAction
# Create your views here.
def index(request):
    

    #team_list = Team.objects.all().order_by('-name')[:15]
    '''
    team_list =getTeams()
    context = {'team_list': team_list}  
    '''
    context = {'team_list': getTeams()}      
    return render(request, 'team/index.html', context)


def teamDetail(request,team_id):
    #team = get_object_or_404(Team, pk=team_id)
    team=getTeamById(team_id)
    return render(request, 'team/team_detail.html', {'team': team})



def playerDetail(request,team_id,player_id):
    '''
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    '''
    team=getTeamById(team_id)
    player=getPlayerById(player_id)
    player_set=team.player_set.all()
    #print(player_set,'player set')
    return render(request, 'team/player.html', {'player': player,
                                                'team':team,
                                                'player_set':player_set})    

def mark(request,team_id,player_id):
    '''
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    '''
    
    player=getPlayerById(player_id)
    new_mark = float(request.POST['mark_input'])
    
    '''
    ori_mark = player.ave_mark
    
    mt=player.mark_times 
    
    print('origin ',ori_mark)
    print('new    ',new_mark)
    print('times  ',mt)
    if ori_mark == 0:
        player.ave_mark = new_mark
    else:
        player.ave_mark = (ori_mark*mt+new_mark)/(mt+1)
        
    player.mark_times =mt+1
    '''
    
    '''
    player.setNewAveMark(new_mark)
    player.save()
    '''
    playerAction.setNewMark(player,new_mark)
    #return render(request, 'team/player.html', {'player': player,'team':team})  
    return HttpResponseRedirect(reverse('team:player', args=(team_id,player_id)))
    
    