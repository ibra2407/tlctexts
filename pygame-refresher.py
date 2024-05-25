import pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Demo for TLC')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Define fonts
font = pygame.font.SysFont(None, 35)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Shapes' initial positions
rect_x, rect_y = 100, 250
ellipse_x, ellipse_y = 300, 250
polygon_points = [(500, 250), (550, 225), (600, 250), (600, 300), (550, 325), (500, 300)]
shape_color = blue

# Control the rectangle
controlled_shape = 'rect'

# Game state
game_state = "blue"

def draw_shapes(color):
    """ Draw a rectangle, an ellipse, and a polygon (hexagon). """
    pygame.draw.rect(screen, color, (rect_x, rect_y, 100, 50))
    pygame.draw.ellipse(screen, color, (ellipse_x, ellipse_y, 100, 50))
    pygame.draw.polygon(screen, color, polygon_points)

def move_controlled_shape():
    """ Move the controlled shape using arrow keys. """
    keys = pygame.key.get_pressed()
    global rect_x, rect_y

    if controlled_shape == 'rect':
        if keys[pygame.K_UP]:
            rect_y -= 1
        if keys[pygame.K_DOWN]:
            rect_y += 1
        if keys[pygame.K_LEFT]:
            rect_x -= 1
        if keys[pygame.K_RIGHT]:
            rect_x += 1

# Main loop flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                game_state = "blue"
                shape_color = blue
            if event.key == pygame.K_r:
                game_state = "red"
                shape_color = red

    # Fill the background
    screen.fill(white)

    # Draw shapes with the current color
    draw_shapes(shape_color)

    # Move the controlled shape
    move_controlled_shape()

    # Display game state and controlled shape coordinates
    draw_text(f"Game State: {game_state}", font, black, screen, screen_width // 2, 30)
    if controlled_shape == 'rect':
        draw_text(f"Rect Position: ({rect_x}, {rect_y})", font, black, screen, screen_width // 2, 70)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
