def print_grid(snake,dir,food_cell):
    grid = [["." for _ in range(6)] for _ in range(6)]
    for cur in snake[1:]:
        grid[cur[0]][cur[1]] = "0"

    head = snake[0]
    x,y = food_cell[0]
    grid[x][y] = "*"

    if snake:
        head = snake[0]
        if dir == 'U': symbol = '^'
        elif dir == 'D': symbol = 'v'
        elif dir == 'L': symbol = '<'
        else: symbol = '>'
        grid[head[0]][head[1]] = symbol

    for row in grid:
        print(' '.join(row))


def main():
    snake = [(0,0)]
    allcell = [(i,j) for i in range(6) for j in range(6)]
    allcell.remove((0,0))
    foodcell = [(1,5),(2,0),(5,2),(3,1)]
    dir = "R"

    print_grid(snake,dir,foodcell)
    
    while True:
        new_dir = input("Enter New Direction(U/D/L/R):")
        dx,dy = 0,0
        if new_dir=="U": dx = -1
        if new_dir=="D": dx = 1
        if new_dir=="L":dy = -1
        if new_dir=="R":dy = 1

        
        new_head = (snake[0][0]+dx , snake[0][1]+dy)
        print(new_head)
        if not (0 <= new_head[0] < 6 and 0 <= new_head[1] < 6):
            print("Game Over: Hit the wall!")
            break
        if new_head in snake[1:]:
            print("bit itself")
            break
 
        food =  new_head == foodcell[0]
        if not food:
            snake.pop()
        new_snake = [new_head]+snake
        if food:
            foodcell.pop(0)

        snake = new_snake
        dir = new_dir
        print_grid(snake,dir,foodcell)

if __name__ == "__main__":
    main()



        




