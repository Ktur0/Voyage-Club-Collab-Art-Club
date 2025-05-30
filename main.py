import pygame

pygame.init()

# Set up screen
widthSr, heightSr = 1280, 720
screen = pygame.display.set_mode((widthSr, heightSr))

run = True

# Mouse
xMouse, yMouse = 0, 0
mouseSize = 20
mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

# Main loop
while run:

    # Update mouse
    xMouse, yMouse = pygame.mouse.get_pos()
    mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Update screen
    pygame.display.update()
    
pygame.quit()