from django.db import models
import datetime


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=10)
    team_id = models.ForeignKey(Team)
    ave_mark = models.FloatField(default=0)
    mark_times = models.IntegerField(default=0)
    
    @property
    def average_mark(self):
        return self.ave_mark

    @average_mark.setter
    def average_mark(self, value):
        if type(value) is not float:
            raise TypeError('not float,ave_mark should be float')
        if value < 0 or value >10:
            raise ValueError('invalid  range, ave_mark should be in 0 to 10') 
        self.ave_mark = value
    
    def __str__(self):  # Python 3: def __str__(self):
        return self.name
    
    def setNewAveMark(self, new_mark):
        if new_mark>10 or new_mark<0:
            pass
        
        ori_mark = self.average_mark
        mt=self.mark_times 
        '''
        print('origin ', ori_mark)
        print('new    ', new_mark)
        print('times  ', mt)
        '''
        if ori_mark == 0:
            self.average_mark = round(new_mark, 1)
        else:
            self.average_mark = round( (ori_mark*mt+new_mark)/(mt+1), 1)
        
            self.mark_times = mt+1
        pass
