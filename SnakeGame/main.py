import random

def print_grid(snake, direction, food_list):
    grid = [['.' for _ in range(6)] for _ in range(6)]
    
    # Place food
    for (r, c) in food_list:
        grid[r][c] = '*'
    
    # Place snake body (all segments except head)
    for segment in snake[1:]:
        r, c = segment
        grid[r][c] = 'O'
    
    # Place snake head
    if snake:
        head = snake[0]
        if direction == 'U': symbol = '^'
        elif direction == 'D': symbol = 'v'
        elif direction == 'L': symbol = '<'
        else: symbol = '>'
        grid[head[0]][head[1]] = symbol
    
    # Print grid
    for row in grid:
        print(' '.join(row))

def main():
    snake = [(0, 0)]
    direction = 'R'
    all_cells = [(i, j) for i in range(6) for j in range(6)]
    all_cells.remove((0, 0))
    food_list = random.sample(all_cells, 3) # number of food in grid
    
    print_grid(snake, direction, food_list)
    
    while True:
        move = input("Enter move (U, D, L, R): ").strip().upper()
        if move not in ['U', 'D', 'L', 'R']:
            print("Invalid move! Use U, D, L, R.")
            continue
            
        new_direction = move
        dr, dc = 0, 0
        if new_direction == 'U': dr = -1
        elif new_direction == 'D': dr = 1
        elif new_direction == 'L': dc = -1
        elif new_direction == 'R': dc = 1
        
        head = snake[0]
        new_head = (head[0] + dr, head[1] + dc)
        
        # Wall collision check
        if not (0 <= new_head[0] < 6 and 0 <= new_head[1] < 6):
            print("Game Over: Hit the wall!")
            break
        
        # Check if food was eaten
        ate_food = new_head in food_list
        
        # Create new snake
        new_snake = [new_head] + snake
        
        # If didn't eat food, remove tail to maintain length
        if not ate_food:
            new_snake.pop()
        
        # Self collision check
        if new_head in new_snake[1:]:
            print("Game Over: Hit itself!")
            break
        
        # Food handling
        if ate_food:
            food_list.remove(new_head)
            # Generate new food if space available
            available = [cell for cell in 
                        [(i, j) for i in range(6) for j in range(6)]
                        if cell not in new_snake and cell not in food_list]
            if available:
                food_list.append(random.choice(available))
        
        # Update game state
        snake = new_snake
        direction = new_direction
        print_grid(snake, direction, food_list)

if __name__ == "__main__":
    main()