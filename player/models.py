from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=10)
    team_id = models.ForeignKey(Team)
    ave_mark = models.IntegerField(default=0)
    mark_times = models.IntegerField(default=0)
    
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.name
    
    
''' 
def insert_player_data():
    player=[x for x in range(4)]
    player=Team.objects.get(pk=111)
    player[0]=Player(id=11110,name='Lionel Messi',team_id=player,ave_mark=0,mark_time=0)
    player[1]=Player(id=11114,name='Javier Mascherano',team_id=player,ave_mark=0,mark_time=0)
    player[2]=Player(id=11101,name='Sergio Romero',team_id=player,ave_mark=0,mark_time=0)
    player[3]=Player(id=11116,name='Marcos Rojo',team_id=player,ave_mark=0,mark_time=0)
    (x.save() for x in player)
    print('insert_player_data end')
    pass

insert_player_data()
'''