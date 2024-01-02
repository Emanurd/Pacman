

def eat_ghost(power_pellet_active: bool, touching_ghost: bool):
   
    if power_pellet_active is True and touching_ghost is True: 
        return True
    if power_pellet_active is False and touching_ghost is False:
        return False
    if power_pellet_active is  False and touching_ghost is True:
        return False
    
    return False


def score(touching_power_pellet, touching_dot):
    
    if touching_power_pellet is True and touching_dot is True:
        return True
    if touching_power_pellet is False and touching_dot is True:
        return True
    if touching_power_pellet is True and touching_dot is False:
        return True
    
    return False


def lose(power_pellet_active, touching_ghost):
    
    if power_pellet_active is True and touching_ghost is True:
        return False
    if power_pellet_active is False and touching_ghost is True:
        return True
    if power_pellet_active is True and touching_ghost is False:
        return False
    
    return False 
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    
    placar = lose(power_pellet_active, touching_ghost)
    if has_eaten_all_dots is True and placar is False:
        return True
    return False
    
    
