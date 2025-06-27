import pygame
import webbrowser

# Buttons for start screen
VoyageLogoBut = pygame.Rect(1211, 20, 57, 57)
ArtLogoBut = pygame.Rect(1134, 20, 57, 57)
StartBut = pygame.Rect(575, 520, 130, 130)

# Mouse
xMouse, yMouse = 0, 0
mouseSize = 20
mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

# Check clickable on club logos
def clickClubButton(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseHB.colliderect(VoyageLogoBut):
                webbrowser.open("https://www.facebook.com/voyage.stc")
            if mouseHB.colliderect(ArtLogoBut):
                webbrowser.open("https://www.facebook.com/ArtclubTHD")