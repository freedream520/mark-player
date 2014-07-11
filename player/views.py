
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from player.models import *
# Create your views here.
def index(request):
    

    team_list = Team.objects.all().order_by('-name')[:10]
    context = {'team_list': team_list}         
    return render(request, 'team/index.html', context)


def teamDetail(request,team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'team/team_detail.html', {'team': team})



def playerDetail(request,team_id,player_id):
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'team/player.html', {'player': player,
                                                'team':team})    

def mark(request,team_id,player_id):
    print('in mark function')
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    ori_mark = player.ave_mark
    new_mark = int(request.POST['mark_input'])
    mt=player.mark_times 
    
    print(ori_mark)
    print(new_mark)
    print(mt)
    if ori_mark == 0:
        player.ave_mark = new_mark
    else:
        player.ave_mark = (ori_mark*mt+new_mark)/(mt+1)
        
    player.mark_times =mt+1
    
    player.save()
    #return render(request, 'team/player.html', {'player': player,'team':team})  
    return HttpResponseRedirect(reverse('team:player', args=(team_id,player_id)))
    
    
    '''  
    try:
        selected_player= team.choice_set.get(pk=request.POST['selected_player'])
    except (KeyError, Player.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'team/team_detail.html', {'team': team,
                                                         'error_message': "no this player.",})
    
    else:   
        ori_mark = selected_player.ave_mark
        new_mark = request.POST['mark_input']
        selected_player.mark_times +=1
        if ori_mark == 0:
            selected_player.ave_mark = new_mark
        else:
            selected_player.ave_mark = (ori_mark+new_mark)/selected_player.mark_times
    
        selected_player.save()
        return render(request, 'team/player.html', {'player': selected_player,
                                                'team':team})    
    '''