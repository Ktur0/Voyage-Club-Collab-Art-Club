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

# Start menu
StrMenuScr = True

# Buttons
VoyageLogoBut = pygame.Rect(0, 0, 50, 50)
ArtLogoBut = pygame.Rect(0, 0, 50, 50)

# Story menu
StoryMenuScr = False

# Gameplay menu
GameMenuScr = False

# Print screen menu
PrintScrMenuScr = False


# Main loop
while run:

    # Update mouse
    xMouse, yMouse = pygame.mouse.get_pos()
    mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Start menu logic
    if StrMenuScr:
        screen.fill((0, 0, 0))  # Clear screen with black

        # Draw buttons
        pygame.draw.rect(screen, (255, 0, 0), VoyageLogoBut)
        pygame.draw.rect(screen, (0, 255, 0), ArtLogoBut)


    elif StoryMenuScr:
        # Game logic can go here
        screen.fill((50, 50, 50))  # Fill with gray for game screen
    
    elif GameMenuScr:
        # Game logic can go here
        screen.fill((100, 100, 100))
    
    elif PrintScrMenuScr:
        # Print screen logic can go here
        screen.fill((150, 150, 150))
    
    # Update screen
    pygame.display.update()
    
pygame.quit()