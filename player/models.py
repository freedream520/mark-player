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
    
    def setNewAveMark(self,new_mark):
        if new_mark>10 or new_mark<0:
            pass
        
        ori_mark = self.ave_mark
        mt=self.mark_times 
        
        print('origin ',ori_mark)
        print('new    ',new_mark)
        print('times  ',mt)
        
        if ori_mark == 0:
            self.ave_mark = new_mark
        else:
            self.ave_mark = (ori_mark*mt+new_mark)/(mt+1)
        
            self.mark_times =mt+1
        pass
