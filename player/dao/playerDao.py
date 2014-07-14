from django.shortcuts import  get_object_or_404
from player.models import Player


def getPlayerById(player_id):
    return get_object_or_404(Player, pk=player_id)