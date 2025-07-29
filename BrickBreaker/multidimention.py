import sys

class BrickBreaker:
    def __init__(self, size=7, brick_positions=None):
        self.size = size
        self.grid = []
        self.ball_pos = (size-1, size//2)  # Start in middle of bottom row
        self.ball_lives = 5
        self.ball_direction = None  # Track current direction for bouncing
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
        
        # If ball is already moving (from previous bounce), continue in that direction
        if self.ball_direction:
            direction = self.ball_direction
        else:
            # Set initial direction
            directions = {
                'St': (-1, 0),   # Straight up
                'Lt': (-1, -1),  # Diagonal left
                'Rt': (-1, 1)    # Diagonal right
            }
            
            if direction not in directions:
                print("Invalid direction! Use St, Lt, or Rt.")
                return
            
            dr, dc = directions[direction]
            self.ball_direction = (dr, dc)
        
        # Remove ball from current position
        if self.ball_pos[0] == self.size-1:
            self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'g'
        else:
            self.grid[self.ball_pos[0]][self.ball_pos[1]] = ' '
        
        dr, dc = self.ball_direction
        new_row, new_col = self.ball_pos[0] + dr, self.ball_pos[1] + dc
        
        # Check for collisions
        while True:
            # Wall collision - bounce logic
            if self.grid[new_row][new_col] == 'w':
                # Determine which wall was hit and bounce appropriately
                if new_row == 0:  # Top wall
                    dr = 1  # Reverse vertical direction
                elif new_row == self.size-1:  # Bottom wall
                    dr = -1
                    self.ball_lives -= 1  # Lose a life when hitting bottom
                if new_col == 0:  # Left wall
                    dc = 1  # Reverse horizontal direction
                elif new_col == self.size-1:  # Right wall
                    dc = -1
                
                self.ball_direction = (dr, dc)
                new_row, new_col = self.ball_pos[0] + dr, self.ball_pos[1] + dc
                continue
            
            # Brick collision
            if self.grid[new_row][new_col].isdigit():
                brick_strength = int(self.grid[new_row][new_col])
                brick_strength -= 1
                
                if brick_strength == 0:
                    # Brick disappears
                    self.grid[new_row][new_col] = ' '
                    # Ball continues in same direction
                    self.ball_pos = (new_row, new_col)
                    self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                    self.ball_direction = (dr, dc)  # Continue same direction
                else:
                    # Brick remains
                    self.grid[new_row][new_col] = str(brick_strength)
                    # Ball bounces back (reverse direction)
                    self.ball_direction = (-dr, -dc)
                    # Return ball to starting position if it was a direct hit from below
                    if self.ball_pos[0] == self.size-1:
                        self.ball_pos = (self.size-1, self.size//2)
                        self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                        self.ball_direction = None  # Reset for next move
                    else:
                        # For bounces during flight, continue with new direction
                        self.ball_pos = (self.ball_pos[0] - dr, self.ball_pos[1] - dc)
                        self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                break
            
            # Empty space or ground
            if self.grid[new_row][new_col] in (' ', 'g'):
                self.ball_pos = (new_row, new_col)
                self.grid[self.ball_pos[0]][self.ball_pos[1]] = 'o'
                # If ball reaches ground without hitting anything, reset
                if new_row == self.size-1:
                    self.ball_direction = None
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