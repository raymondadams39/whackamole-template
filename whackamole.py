import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 512
GRID_SIZE = 32
COLUMNS, ROWS = 20, 16

def move_mole():
    # Randomly choose a new x and y position within the grid
    x = random.randrange(COLUMNS) * GRID_SIZE
    y = random.randrange(ROWS) * GRID_SIZE
    return x, y

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        # Move mole to a new random position if clicked
                        mole_x, mole_y = move_mole()
            screen.fill("light green")
            #vertical lines
            for i in range(20):
                pygame.draw.line(screen, "dark green", (i * GRID_SIZE, 0), (i * GRID_SIZE, SCREEN_HEIGHT))
            #horizontal lines
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, i * GRID_SIZE), (SCREEN_WIDTH, i * GRID_SIZE))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
