import unittest

def propagate(list_of_positions_before):
    #first_x_after_propagate
    #second_x_after_propagate

    first_x_before = list_of_positions_before[0];
    second_x_before = list_of_positions_before[0];

    # calculez toti vecinii lui x
    hash_x = turn_tuple_into_hash(first_x_before['coordinates']);

    list_of_neighbours += [ (i,j) for i in range(hash_x['x']-1,hash_x['y']+2) 
                            for j in range(hash_x['x']-1,hash_x['y']+2) 
                            if (i,j) != (hash_x['x'],hash_x['y']) ]

    # verific daca coordinatele lui second_x se afla printre vecinii lui first_x
    for tuple_y in list_of_neighbours:
        if tuple_y == second_x_before['coordinates']
           # actualizare first_x_after_propagate si second_x_after_propagate 
	

    return [first_x_after_propagate, second_x_after_propagate]


class FiveInARowTestSuite(unittest.TestCase):
    
    def test_correctness_of_propagate(self):
        # define input
        first_x_before = {'coordinates':(0,0), 'contiguous':{'contiguous_to_the_east':[(0,0)], 'contiguous_to_the_west':[(0,0)]}}
        first_x_after = {'coordinates':(0,0), 'contiguous':{'contiguous_to_the_east':[(0,0),(1,0)], 'contiguous_to_the_west':[(0,0)]}}
        second_x_before = {'coordinates':(1,0), 'contiguous':{'contiguous_to_the_east':[(0,0)], 'contiguous_to_the_west':[(0,0)]}}
        second_x_after = {'coordinates':(1,0), 'contiguous':{'contiguous_to_the_east':[(1,0)], 'contiguous_to_the_west':[(0,0),(1,0)]}}
        list_of_positions_before = [first_x_before, second_x_before]

        # apply transformation
        actual_resulting_list = propagate(list_of_positions_before)

        # state expectation
        expected_resulting_list = [first_x_after, second_x_after]
        self.assertEqual(expected_resulting_list, actual_resulting_list)

unittest.main()
