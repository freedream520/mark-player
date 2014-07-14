from django.shortcuts import  get_object_or_404
from player.models import Team
'''
get data for DB
'''
def getTeamById(team_id):
    return get_object_or_404(Team, pk=team_id)

def getTeams(t_number=15):
    return Team.objects.all().order_by('-name')[:t_number]

