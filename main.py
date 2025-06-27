import pygame
import webbrowser
import os

pygame.init()

# Set up screen
screenInfo = pygame.display.Info() 
pygame.display.set_caption("Voyage Club - Art Club")
widthSr, heightSr = screenInfo.current_w, screenInfo.current_h
screen = pygame.display.set_mode((widthSr, heightSr))
currentScreen = "StartMenu"
run = True

# Colors    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# Gameplay menu
CharacterFrame = pygame.Rect(164, 62, 456, 628) 
ItemFrame = pygame.Rect(694, 105, 485, 585)

# Buttons for gameplay menu
CameraBut = pygame.Rect(26, 257, 88, 88)
HomeGameplayBut = pygame.Rect(26, 375, 88, 88)
ShirtBut = pygame.Rect(1144, 120, 75, 75)
PaintBut = pygame.Rect(1144, 215, 75, 75)
ShoeBut = pygame.Rect(1144, 310, 75, 75)
HatBut = pygame.Rect(1144, 405, 75, 75)
SparePartsBut = pygame.Rect(1144, 500, 75, 75)
EmotionBut = pygame.Rect(1144, 595, 75, 75)

# Buttons for start screen
VoyageLogoBut = pygame.Rect(1211, 20, 57, 57)
ArtLogoBut = pygame.Rect(1134, 20, 57, 57)
StartBut = pygame.Rect(575, 520, 130, 130)

# Print screen menu
PhotoFrame = pygame.Rect(412, 62, 456, 628)

# Buttons for print screen menu
DownloadBut = pygame.Rect(26, 198, 88, 88)
ReturnBut = pygame.Rect(26, 316, 88, 88)
HomePrintBut = pygame.Rect(26, 434, 88, 88)
NextPrintBut = pygame.Rect(1185, 625, 70, 70)
PreviousPrintBut = pygame.Rect(1095, 625, 70, 70)

# Story menu
StoryFrame1 = pygame.Rect(46, 46, 571, 291)
StoryFrame2 = pygame.Rect(663, 46, 571, 291)  
StoryFrame3 = pygame.Rect(46, 383, 571, 291)  
StoryFrame4 = pygame.Rect(663, 383, 571, 291)  

# Buttons for story menu
StoryMenuNextBut = pygame.Rect(1167, 607, 88, 88) 

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

# Image 
menuBackground = pygame.image.load("Asset/ACAN-MENU/StartMenu.png")

# Mouse
xMouse, yMouse = 0, 0
mouseSize = 20
mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

def scaleRect(rect):
    rect.x = int(rect.x * (widthSr / screenInfo.current_w))
    rect.y = int(rect.y * (heightSr / screenInfo.current_h))
    rect.width = int(rect.width * (widthSr / screenInfo.current_w))
    rect.height = int(rect.height * (heightSr / screenInfo.current_h))  
    return rect

def clickClubButton(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseHB.colliderect(VoyageLogoBut):
                webbrowser.open("https://www.facebook.com/voyage.stc")
            if mouseHB.colliderect(ArtLogoBut):
                webbrowser.open("https://www.facebook.com/ArtclubTHD")

def countFilesInDirectory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# Main loop
while run:

    # Update mouse
    xMouse, yMouse = pygame.mouse.get_pos()
    mouseHB = pygame.Rect(xMouse, yMouse, mouseSize, mouseSize)

    events = pygame.event.get()

    # Event
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    
    # Start menu logic
    if currentScreen == "StartMenu":
        screen.fill(WHITE)  # Clear screen with black

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over the start button
                if mouseHB.colliderect(StartBut):
                    currentScreen = "StoryMenu"
        
        screen.blit(menuBackground, scaleRect(BackGround))  # Draw background image

        # # Draw buttons
        # pygame.draw.circle(screen, RED, (VoyageLogoBut.centerx, VoyageLogoBut.centery), VoyageLogoBut.width // 2)
        # pygame.draw.circle(screen, YELLOW, (ArtLogoBut.centerx, ArtLogoBut.centery), ArtLogoBut.width // 2)
        # pygame.draw.circle(screen, GREY, (StartBut.centerx, StartBut.centery), StartBut.width // 2)
        
        
    elif currentScreen == "StoryMenu":
        screen.fill(WHITE)  # Fill with gray for game screen

        clickClubButton(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for next button click
                if mouseHB.colliderect(StoryMenuNextBut):
                   currentScreen = "GameMenu"

        # Draw story frames
        pygame.draw.rect(screen, GREY, StoryFrame1)
        pygame.draw.rect(screen, GREY, StoryFrame2)
        pygame.draw.rect(screen, GREY, StoryFrame3)
        pygame.draw.rect(screen, GREY, StoryFrame4)

        # Draw next button
        pygame.draw.circle(screen, RED, (StoryMenuNextBut.centerx, StoryMenuNextBut.centery), StoryMenuNextBut.width // 2)
        
    elif currentScreen == "GameMenu":
        
        screen.fill(WHITE)

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:
            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(CameraBut):
                    currentScreen = "PrintScreenMenu"
                
                if mouseHB.colliderect(HomeGameplayBut):
                    currentScreen = "StartMenu"

        # Draw character and item frames
        pygame.draw.rect(screen, BLUE, CharacterFrame)
        pygame.draw.rect(screen, RED, ItemFrame)

        # Draw buttons
        pygame.draw.circle(screen, RED, (VoyageLogoBut.centerx, VoyageLogoBut.centery), VoyageLogoBut.width // 2)
        pygame.draw.circle(screen, YELLOW, (ArtLogoBut.centerx, ArtLogoBut.centery), ArtLogoBut.width // 2)
        pygame.draw.circle(screen, GREEN, (CameraBut.centerx, CameraBut.centery), CameraBut.width // 2)
        pygame.draw.circle(screen, YELLOW, (HomeGameplayBut.centerx, HomeGameplayBut.centery), HomeGameplayBut.width // 2)
        pygame.draw.circle(screen, GREY, (ShirtBut.centerx, ShirtBut.centery), ShirtBut.width // 2)
        pygame.draw.circle(screen, GREY, (PaintBut.centerx, PaintBut.centery), PaintBut.width // 2)
        pygame.draw.circle(screen, GREY, (ShoeBut.centerx, ShoeBut.centery), ShoeBut.width // 2)
        pygame.draw.circle(screen, GREY, (HatBut.centerx, HatBut.centery), HatBut.width // 2)
        pygame.draw.circle(screen, GREY, (SparePartsBut.centerx, SparePartsBut.centery), SparePartsBut.width // 2)
        pygame.draw.circle(screen, GREY, (EmotionBut.centerx, EmotionBut.centery), EmotionBut.width // 2)
        

    elif currentScreen == "PrintScreenMenu":
        # Print screen logic can go here
        screen.fill(WHITE)
        
        # Draw photo frame
        pygame.draw.rect(screen, GREY, PhotoFrame)

        # Draw buttons
        pygame.draw.circle(screen, RED, (VoyageLogoBut.centerx, VoyageLogoBut.centery), VoyageLogoBut.width // 2)
        pygame.draw.circle(screen, YELLOW, (ArtLogoBut.centerx, ArtLogoBut.centery), ArtLogoBut.width // 2)
        pygame.draw.circle(screen, GREEN, (DownloadBut.centerx, DownloadBut.centery), DownloadBut.width // 2)
        pygame.draw.circle(screen, YELLOW, (ReturnBut.centerx, ReturnBut.centery), ReturnBut.width // 2)
        pygame.draw.circle(screen, GREY, (HomePrintBut.centerx, HomePrintBut.centery), HomePrintBut.width // 2)
        pygame.draw.circle(screen, GREY, (NextPrintBut.centerx, NextPrintBut.centery), NextPrintBut.width // 2)
        pygame.draw.circle(screen, GREY, (PreviousPrintBut.centerx, PreviousPrintBut.centery), PreviousPrintBut.width // 2)

        # Check for button clicks
        clickClubButton(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(DownloadBut):
                    subsurface = screen.subsurface(PhotoFrame).copy() 
                    pygame.image.save(subsurface, "SavePicture/Screenshot"+str(countFilesInDirectory("SavePicture")) + ".png")

                if mouseHB.colliderect(ReturnBut):
                    currentScreen = "GameMenu"
                     
                if mouseHB.colliderect(HomePrintBut):
                    currentScreen = "StartMenu"
        
    # Update screen
    pygame.display.update()
    
pygame.quit()