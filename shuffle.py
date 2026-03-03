import random
def get_moves(zero_index):
    moves = []
    if zero_index > 2:
        moves.append(zero_index - 3)
    if zero_index < 6:
        moves.append(zero_index + 3)
    if zero_index % 3 != 0:
        moves.append(zero_index - 1)
    if zero_index % 3 != 2:
        moves.append(zero_index + 1)
    return moves
def random_table():
    table = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    n = random.randint(5, 25)
    
    for _ in range(n):
        zero_index = table.index(0)
        legal = get_moves(zero_index)
        move = random.choice(legal)
        
        table[zero_index], table[move] = table[move], table[zero_index]
    
    return tuple(table)