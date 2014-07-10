
from django.shortcuts import render , get_object_or_404


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