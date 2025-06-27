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

def scale_rect(xr, yr, wr, hr):
    return pygame.Rect(int(xr* widthSr), int(yr * heightSr), int(wr * widthSr), int(hr * heightSr))

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

        # Images for start screen
        StartMenuBackground = pygame.image.load("Asset/ACAN-MENU/StartMenu.png")
        StartButton = pygame.image.load("Asset/Button/StartButton.png")

        # UI for start screen
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        StartBut = scale_rect(0.45, 0.72, 0.1, 0.18)

        screen.blit(pygame.transform.smoothscale(StartMenuBackground, (widthSr, heightSr)), (0, 0))  # Fill with start menu background
        screen.blit(pygame.transform.smoothscale(StartButton, (StartBut.width, StartBut.height)), (StartBut.x, StartBut.y))  # Draw start button

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over the start button
                if mouseHB.colliderect(StartBut):
                    currentScreen = "StoryMenu"
          
        # # Draw buttons
        # pygame.draw.circle(screen, RED, (VoyageLogoBut.centerx, VoyageLogoBut.centery), VoyageLogoBut.width // 2)
        # pygame.draw.circle(screen, YELLOW, (ArtLogoBut.centerx, ArtLogoBut.centery), ArtLogoBut.width // 2)
        # pygame.draw.circle(screen, GREY, (StartBut.centerx, StartBut.centery), StartBut.width // 2)
        
    elif currentScreen == "StoryMenu":

        # Images for story screen
        StoryMenuNextButtonImage = pygame.image.load("Asset/Button/NextButton.png")

        StoryImage1 = pygame.image.load("Asset/COMIC/1.png")
        StoryImage2 = pygame.image.load("Asset/COMIC/2.png")
        StoryImage3 = pygame.image.load("Asset/COMIC/3.png")   
        StoryImage4 = pygame.image.load("Asset/COMIC/4.png")

        # UI for story screen
        StoryMenuNextBut = scale_rect(0.91, 0.87, 0.07, 0.12)
        StoryFrame1 = scale_rect(0.036, 0.06, 0.44, 0.4)
        StoryFrame2 = scale_rect(0.52, 0.06, 0.44, 0.4)
        StoryFrame3 = scale_rect(0.036, 0.53, 0.44, 0.4)
        StoryFrame4 = scale_rect(0.52, 0.53, 0.44, 0.4)

        # Fill with story menu background
        screen.fill(WHITE)
        screen.blit(pygame.transform.smoothscale(StoryImage1, (widthSr, heightSr)), (0,0))  # Draw story image 1
        screen.blit(pygame.transform.smoothscale(StoryImage2, (widthSr, heightSr)), (0,0))  # Draw story image 2
        screen.blit(pygame.transform.smoothscale(StoryImage3, (widthSr, heightSr)), (0,0))  # Draw story image 3
        screen.blit(pygame.transform.smoothscale(StoryImage4, (widthSr, heightSr)), (0,0))  # Draw story image 4
        screen.blit(pygame.transform.smoothscale(StoryMenuNextButtonImage, (StoryMenuNextBut.width, StoryMenuNextBut.height)), (StoryMenuNextBut.x, StoryMenuNextBut.y))

        clickClubButton(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for next button click
                if mouseHB.colliderect(StoryMenuNextBut):
                   currentScreen = "GameMenu"

        # Draw story frames
        # pygame.draw.rect(screen, GREY, StoryFrame1)
        # pygame.draw.rect(screen, GREY, StoryFrame2)
        # pygame.draw.rect(screen, GREY, StoryFrame3)
        # pygame.draw.rect(screen, GREY, StoryFrame4)

        # Draw next button
        # pygame.draw.circle(screen, RED, (StoryMenuNextBut.centerx, StoryMenuNextBut.centery), StoryMenuNextBut.width // 2)
        
    elif currentScreen == "GameMenu":

        # UI for gameplay screen
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        CameraBut = scale_rect(0.02, 0.36, 0.07, 0.12)
        HomeGameplayBut = scale_rect(0.02, 0.52, 0.07, 0.12)
        ShirtBut = scale_rect(0.89, 0.17, 0.06, 0.1)
        PaintBut = scale_rect(0.89, 0.30, 0.06, 0.1)
        ShoeBut = scale_rect(0.89, 0.43, 0.06, 0.1)
        HatBut = scale_rect(0.89, 0.56, 0.06, 0.1)
        SparePartsBut = scale_rect(0.89, 0.69, 0.06, 0.1)
        EmotionBut = scale_rect(0.89, 0.82, 0.06, 0.1)

        CharacterFrame = scale_rect(0.13, 0.09, 0.36, 0.85)
        ItemFrame = scale_rect(0.54, 0.14, 0.38, 0.78)
        
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

        # UI for print screen menu
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        ReturnBut = scale_rect(0.02, 0.45, 0.07, 0.12)
        HomePrintBut = scale_rect(0.02, 0.61, 0.07, 0.12)
        NextPrintBut = scale_rect(0.925, 0.87, 0.055, 0.1)
        PreviousPrintBut = scale_rect(0.855, 0.87, 0.055, 0.1)
        PhotoFrame = scale_rect(0.32, 0.09, 0.36, 0.85)
        DownloadBut = scale_rect(0.02, 0.28, 0.07, 0.12)

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