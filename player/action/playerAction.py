
def setNewMark(player,new_mark):
    mark_time = player.setNewAveMark(new_mark)
    player.save()
    return mark_time
    
