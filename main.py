from Table_Print import print_table
from shuffle import random_table
from A_STAR import a_star, get_path, Node
start_state = random_table()
start_node = Node(start_state)
goal_state = a_star(start_node)
if goal_state:
    solution_steps = get_path(goal_state)
    print(f"Goal reached in {len(solution_steps) - 1} moves!")
    
    for i, board in enumerate(solution_steps):
        print(f"Step {i}:")
        print_table(board)
else:
    print("No solution found.")

