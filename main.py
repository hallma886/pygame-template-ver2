# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption("Draw Lines Without Using a Function")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main(screen):
    # Arguments for first line 
    start_pos1 = [150, 150]
    end_pos1 = [350, 500]
    line_color1 = config.GREEN
    line_thickness1 = 10  # Set line width (thickness) in pixels

    # Arguments for second line 
    start_pos2 = [400, 350]
    end_pos2 = [225, 425]
    line_color2 = config.BLUE
    line_thickness2 = 6  # Set line width (thickness) in pixels

    # Arguments for third line 
    start_pos3 = [350, 250]
    end_pos3 = [250, 600]
    line_color3 = config.RED
    line_thickness3 = 19  # Set line width (thickness) in pixels

    # Arguments for fourth line 
    start_pos4 = [500, 450]
    end_pos4 = [335, 535]
    line_color4 = config.BLACK
    line_thickness4 = 14  # Set line width (thickness) in pixels

        # Arguments for fifth line 
    start_pos5 = [650, 350]
    end_pos5 = [350, 600]
    line_color5 = config.PURPLE
    line_thickness5 = 8  # Set line width (thickness) in pixels

    # Arguments for sixth line 
    start_pos6 = [600, 550]
    end_pos6 = [435, 550]
    line_color6 = config.ORANGE
    line_thickness6 = 16  # Set line width (thickness) in pixels


    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color (optional)
        screen.fill(config.WHITE)  # Assuming you have a WHITE constant in config

        # Draw the lines
        pygame.draw.line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        pygame.draw.line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        pygame.draw.line(screen, line_color3, start_pos3, end_pos3, line_thickness3)
        pygame.draw.line(screen, line_color4, start_pos4, end_pos4, line_thickness4)
        pygame.draw.line(screen, line_color5, start_pos5, end_pos5, line_thickness5)
        pygame.draw.line(screen, line_color6, start_pos6, end_pos6, line_thickness6)
        pygame.display.flip()  # Update the display

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    screen = init_game()  # Initialize the game and get the screen
    main(screen)  # Pass the screen to the main function































