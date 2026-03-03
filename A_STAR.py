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
    
    # Trace back to the start
    while current is not None:
        path.append(current.state) # Store the board configuration
        current = current.parent   # Move to the 'father' node
        
    # The path is currently Goal -> Start, so reverse it
    return path[::-1]

def a_star(start_node):
    # The Frontier: a priority queue containing our nodes
    # Since we added __lt__ to the Node class, heapq knows to sort by f
    frontier = [start_node]
    heapq.heapify(frontier)
    
    # The Explored Set: stores the 'state' tuple to prevent loops
    seen = {start_node.state} 
    
    while frontier:
        # 1. Pop the node with the smallest f(n)
        current_node = heapq.heappop(frontier)
        
        # 2. Check if we reached the goal
        if current_node.state == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return current_node # Trace back using 'parent' later
            
        # 3. Expand: Get indices of legal moves for the blank (0)
        zero_index = current_node.state.index(0)
        legal_indices = get_moves(zero_index) # From your shuffle.py logic
        
        for move_index in legal_indices:
            # Create the new state by swapping
            new_state = list(current_node.state)
            new_state[zero_index], new_state[move_index] = new_state[move_index], new_state[zero_index]
            new_state_tuple = tuple(new_state)
            
            # 4. Only process if we haven't seen this board before
            if new_state_tuple not in seen:
                seen.add(new_state_tuple)
                
                # Create a child node: g increases by 1, parent is current_node
                child = Node(state=new_state_tuple, parent=current_node, g=current_node.g + 1)
                
                # 5. Put on the heap (it sorts automatically based on child.f)
                heapq.heappush(frontier, child)
                
    return None # No solution found





