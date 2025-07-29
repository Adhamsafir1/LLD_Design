import sys

class BrickBreaker:
    def __init__(self, size=7, brick_positions=None):
        self.size = size
        self.grid = []
        self.ball_pos = (size-1, size//2)  # Start in middle of bottom row
        self.ball_lives = 5
        self.initialize_grid(brick_positions)
    
    def initialize_grid(self, brick_positions):
        # Create empty grid
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        
        # Add walls (w) around the perimeter
        for i in range(self.size):
            self.grid[0][i] = 'w'  # Top wall
            self.grid[self.size-1][i] = 'w'  # Bottom wall
            self.grid[i][0] = 'w'  # Left wall
            self.grid[i][self.size-1] = 'w'  # Right wall
        
        # Add ground (g) at bottom
        for i in range(1, self.size-1):
            self.grid[self.size-1][i] = 'g'
        
        # Place ball (o)
        self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
        
        # Add bricks with strength 1 at specified positions
        if brick_positions:
            for (row, col) in brick_positions:
                if 0 < row < self.size-1 and 0 < col < self.size-1:
                    self.grid[row][col] = '1'
    
    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print(f"Ball count: {self.ball_lives}")
    
    def move_ball(self, direction):
        if self.ball_lives <= 0:
            print("Game Over! No lives left.")
            return
        
        directions = {
            'St': (-1, 0),   # Straight up
            'Lt': (-1, -1),  # Diagonal left
            'Rt': (-1, 1)    # Diagonal right
        }
        
        if direction not in directions:
            print("Invalid direction! Use St, Lt, or Rt.")
            return
        
        # Remove ball from current position (replace with ground if it was there)
        if self.ball_pos[0] == self.size-1:
            self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'g'
        else:
            self.grid[self.ball_pos[0]][self.ball_pos[1]] = ' '
        
        # Calculate new position
        dr, dc = directions[direction]
        new_row, new_col = self.ball_pos[0] + dr, self.ball_pos[1] + dc
        
        # Check for collisions
        while True:
            # Wall collision
            if self.grid[new_row][new_col] == 'w':
                self.ball_lives -= 1
                # Return ball to starting position
                self.ball_pos = (self.size-1, self.size//2)
                self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                break
            
            # Brick collision
            if self.grid[new_row][new_col].isdigit():
                brick_strength = int(self.grid[new_row][new_col])
                brick_strength -= 1
                
                if brick_strength == 0:
                    # Brick disappears
                    self.grid[new_row][new_col] = ' '
                    # Ball continues to next position
                    next_row, next_col = new_row + dr, new_col + dc
                    
                    # Check if next position is valid
                    if (0 < next_row < self.size-1 and 
                        0 < next_col < self.size-1 and
                        self.grid[next_row][next_col] in (' ', 'g')):
                        self.ball_pos = (next_row, next_col)
                        self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                    else:
                        # Ball hits another wall or brick
                        self.ball_lives -= 1
                        self.ball_pos = (self.size-1, self.size//2)
                        self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                else:
                    # Brick remains
                    self.grid[new_row][new_col] = str(brick_strength)
                    # Ball returns to starting position
                    self.ball_pos = (self.size-1, self.size//2)
                    self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                break
            
            # Empty space or ground
            if self.grid[new_row][new_col] in (' ', 'g'):
                self.ball_pos = (new_row, new_col)
                self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                break
            
            # Move to next position in path
            new_row += dr
            new_col += dc
    
    def play(self):
        print("Initial grid:")
        self.print_grid()
        
        while self.ball_lives > 0:
            cmd = input("Enter move (St, Lt, Rt): ").strip()
            if cmd.lower() == 'quit':
                break
            self.move_ball(cmd)
            self.print_grid()
            
            # Check if all bricks are destroyed
            if all(cell not in ('1', '2', '3') for row in self.grid for cell in row):
                print("Congratulations! You destroyed all bricks!")
                break

if __name__ == "__main__":
    # Example setup with 6 bricks
    brick_positions = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)]
    game = BrickBreaker(7, brick_positions)
    game.play()