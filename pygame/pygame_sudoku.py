# pygame_sudoku.py

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from sudoku_solver import init_given_table, array, output_table, addnum

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 5
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('5x5 Sudoku Solver')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_col = mouse_x // CELL_SIZE
            clicked_row = mouse_y // CELL_SIZE
            if 0 <= clicked_col < GRID_SIZE and 0 <= clicked_row < GRID_SIZE:
                num_input = input("Enter the number [1-5] for the selected cell: ")
                try:
                    num = int(num_input)
                    if 1 <= num <= 5:
                        addnum(clicked_col + 1, clicked_row + 1, array, num)
                        output_table(array)
                except ValueError:
                    print("Please enter a valid number.")

    # Draw the Sudoku grid
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            num = array[row][col]
            if num != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(num), True, RED)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 3))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
