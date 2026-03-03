import heapq
from shuffle import get_moves
class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state     
        self.parent = parent   
        self.g = g            
        self.h = self.calculate_h1() 
        self.f = self.g + self.h    

    def calculate_h1(self):
        count = 0
        for i in range(len(self.state)):
            value = self.state[i]
            if value != 0: 
                if value != i + 1:
                    count += 1
        return count

    def __lt__(self, other):
        return self.f < other.f
    def calculate_h1(node):
        count = 0
        for i in range(len(node.state)):
         if node.state[i] != 0 and node.state[i] != i+1:
               count += 1
        return count
def get_path(goal_node):
    path = []
    current = goal_node
    
    
    while current is not None:
        path.append(current.state) 
        current = current.parent   
        
    return path[::-1]

def a_star(start_node):
    
    
    frontier = [start_node]
    heapq.heapify(frontier)
    
    
    seen = {start_node.state} 
    
    while frontier:
        
        current_node = heapq.heappop(frontier)
        
        
        if current_node.state == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return current_node 
            
        
        zero_index = current_node.state.index(0)
        legal_indices = get_moves(zero_index) 
        
        for move_index in legal_indices:
            
            new_state = list(current_node.state)
            new_state[zero_index], new_state[move_index] = new_state[move_index], new_state[zero_index]
            new_state_tuple = tuple(new_state)
            
            
            if new_state_tuple not in seen:
                seen.add(new_state_tuple)
                
                
                child = Node(state=new_state_tuple, parent=current_node, g=current_node.g + 1)
                
                
                heapq.heappush(frontier, child)
                
    return None 





