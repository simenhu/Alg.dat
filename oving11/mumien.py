from sys import stdin, stderr

nm = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
prob = [1.0, 0.9, 0.3, 0.1, 0.8, 1.0]

def best_path(nm, prob):
    current_node = 0
    updated_weights = [x for x in range(len(nm))] #list to hold updated max_weights
    updated_weights[0] = prob[0] #sets the max weight of the start node to the start node
    predecesor_list = [None for x in range(len(nm))]
    visited_count = 0
    timer = 0
    while predecesor_list[len(nm)-1] == None:
        #iterates until all nodes have been visited or the max node is neighbour to finnish node
        for n in range(len(nm)): #iterates through new visiteds neigbours
            if nm[current_node][n] == 1 and updated_weights[n] > -1:
                old_value = updated_weights[n] #the old max value for node n
                new_value = updated_weights[current_node]*prob[n] #the new max value for node n
                if new_value > old_value:
                    #if the new value is  bigger than the old value and isnot already visited
                    updated_weights[n] = new_value #updates the weight of the nodes
                    predecesor_list[n] = current_node #

        updated_weights[current_node] = -1 #marks that the node is visited with negative value
        current_node = updated_weights.index(max(updated_weights))
        timer
        visited_count += 1
        timer+=1
        print(timer)
    print(predecesor_list)








#print (best_path(neighbour_matrix, probabilities))

best_path(nm, prob)