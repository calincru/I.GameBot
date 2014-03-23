import random

def turn_hash_into_tuple(hash):
	return (hash['x'],hash['y'])

def turn_tuple_into_hash(tuple):
	return {'x':tuple[0],'y':tuple[1]}

def play_turn(
		player_role,
		owned_by_x,
		owned_by_zero):
	
	list_of_dicts = owned_by_x + owned_by_zero
	list_of_neighbours = []
	for dict in list_of_dicts:
		list_of_neighbours += [ (i,j) for i in range(dict['x']-1,dict['y']+2) 
						  	    for j in range(dict['x']-1,dict['y']+2) if (i,j) != (0,0) ]
			
	list_of_tuples = [ turn_hash_into_tuple(x) for x in list_of_dicts ]
	set_of_dicts = set(list_of_tuples)
	set_of_neighbours = set(list_of_neighbours)

	available_neighbours = set_of_neighbours - set_of_dicts
	list_available_neighbours = list(available_neighbours)
	return turn_tuple_into_hash(random.choice(list_available_neighbours))		
