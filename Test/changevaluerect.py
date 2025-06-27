import pygame

pygame.init()

info = pygame.display.Info()
widthSr, heightSr = info.current_w, info.current_h
screen = pygame.display.set_mode((widthSr, heightSr))
run = True
rect = pygame.Rect(100, 100, 200, 150)  # Example rectangle

def scale_rect(rect):
    """Scale the rectangle based on the current screen size."""
    rect.x = int(rect.x * (widthSr / 800))  # Assuming original width is 800
    rect.y = int(rect.y * (heightSr / 600))  # Assuming original height is 600
    rect.width = int(rect.width * (widthSr / 800))
    rect.height = int(rect.height * (heightSr / 600))

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))  # Fill the screen with white

    pygame.display.flip()