import pygame
import webbrowser
import os
import time

pygame.init()

# Set up screen
screenInfo = pygame.display.Info() 
pygame.display.set_caption("Voyage Club - Art Club")
widthSr, heightSr = screenInfo.current_w, screenInfo.current_h
screen = pygame.display.set_mode((widthSr, heightSr))
currentScreen = "StartMenu"
run = True
yGameTitle = 500

# Colors    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# Images for gameplay screen
modelImage = pygame.image.load("Asset/ACAN-MENU/Model.png")
GameplayBackground = pygame.image.load("Asset/RoomBackGround/GameplayBackGround.png")
CameraButImage = pygame.image.load("Asset/Button/CameraButton.png")
HomeGameplayButImage = pygame.image.load("Asset/Button/HomeButton.png")

# Story Frames
StoryImage1 = pygame.image.load("Asset/COMIC/1.png")
StoryImage2 = ''
StoryImage3 = ''  
StoryImage4 = ''
StoryMenuNextButtonImage = ''

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

        if yGameTitle > 0:
            yGameTitle -= 50

        # Images for start screen
        StartMenuBackground = pygame.image.load("Asset/ACAN-MENU/StartMenu.png")
        StartButton = pygame.image.load("Asset/Button/StartButton.png")
        GameTitle = pygame.image.load("Asset/ACAN-MENU/GameTitle.png")

        # UI for start screen
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        StartBut = scale_rect(0.45, 0.72, 0.1, 0.18)

        screen.blit(pygame.transform.smoothscale(StartMenuBackground, (widthSr, heightSr)), (0, 0))  # Fill with start menu background
        screen.blit(pygame.transform.smoothscale(GameTitle, (widthSr, heightSr)), (0, 0 + yGameTitle))  # Draw game title
        screen.blit(pygame.transform.smoothscale(StartButton, (StartBut.width, StartBut.height)), (StartBut.x, StartBut.y))  # Draw start button

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over the start button
                if mouseHB.colliderect(StartBut):
                    currentScreen = "StoryMenu"
                    startTime = time.time()  # Record the start time for the story menu
          
        # # Draw buttons
        # pygame.draw.circle(screen, RED, (VoyageLogoBut.centerx, VoyageLogoBut.centery), VoyageLogoBut.width // 2)
        # pygame.draw.circle(screen, YELLOW, (ArtLogoBut.centerx, ArtLogoBut.centery), ArtLogoBut.width // 2)
        # pygame.draw.circle(screen, GREY, (StartBut.centerx, StartBut.centery), StartBut.width // 2)
        
    elif currentScreen == "StoryMenu":

        # UI for story screen
        StoryMenuNextBut = scale_rect(0.91, 0.87, 0.07, 0.12)
        StoryFrame1 = scale_rect(0.036, 0.06, 0.44, 0.4)
        StoryFrame2 = scale_rect(0.52, 0.06, 0.44, 0.4)
        StoryFrame3 = scale_rect(0.036, 0.53, 0.44, 0.4)
        StoryFrame4 = scale_rect(0.52, 0.53, 0.44, 0.4)

        if int(time.time() - startTime) == 1:  # Show first image for 1 seconds
            StoryImage2 = pygame.image.load("Asset/COMIC/2.png")
        elif int(time.time() - startTime) == 2:  # Show second image for 2 seconds
            StoryImage3 = pygame.image.load("Asset/COMIC/3.png") 
        elif int(time.time() - startTime) == 3:  # Show third image for 3 seconds
            StoryImage4 = pygame.image.load("Asset/COMIC/4.png")
        elif int(time.time() - startTime) == 4:  # Show fourth image for 4 seconds
            StoryMenuNextButtonImage = pygame.image.load("Asset/Button/NextButton.png")  # Show next button

        # Fill with story menu background
        screen.fill(WHITE)
        screen.blit(pygame.transform.smoothscale(StoryImage1, (widthSr, heightSr)), (0,0))  
        if StoryImage2 != '':
            screen.blit(pygame.transform.smoothscale(StoryImage2, (widthSr, heightSr)), (0,0))
        if StoryImage3 != '':
            screen.blit(pygame.transform.smoothscale(StoryImage3, (widthSr, heightSr)), (0,0))  
        if StoryImage4 != '':
            screen.blit(pygame.transform.smoothscale(StoryImage4, (widthSr, heightSr)), (0,0))
        if StoryMenuNextButtonImage != '':
            screen.blit(pygame.transform.smoothscale(StoryMenuNextButtonImage, (StoryMenuNextBut.width, StoryMenuNextBut.height)), (StoryMenuNextBut.x, StoryMenuNextBut.y))

        clickClubButton(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for next button click
                if mouseHB.colliderect(StoryMenuNextBut):
                   currentScreen = "GameMenu"
        
    elif currentScreen == "GameMenu":

        # UI for gameplay screen
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        CameraBut = scale_rect(0.02, 0.36, 0.07, 0.12)
        HomeGameplayBut = scale_rect(0.02, 0.52, 0.07, 0.12)
        ShirtBut = scale_rect(0.895, 0.175, 0.06, 0.1)
        PaintBut = scale_rect(0.895, 0.31, 0.06, 0.1)
        ShoeBut = scale_rect(0.895, 0.44, 0.06, 0.1)
        HatBut = scale_rect(0.895, 0.575, 0.06, 0.1)
        SparePartsBut = scale_rect(0.895, 0.71, 0.06, 0.1)
        EmotionBut = scale_rect(0.895, 0.84, 0.06, 0.1)

        CharacterFrame = scale_rect(0.13, 0.09, 0.36, 0.85)
        ItemFrame = scale_rect(0.54, 0.14, 0.38, 0.78)
        

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:
            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(CameraBut):
                    currentScreen = "PrintScreenMenu"
                
                if mouseHB.colliderect(HomeGameplayBut):
                    currentScreen = "StartMenu"

                if mouseHB.colliderect(ShirtBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/ShirtSelect.png")
                if mouseHB.colliderect(PaintBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/PaintSelect.png")
                if mouseHB.colliderect(ShoeBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/ShoeSelect.png")
                if mouseHB.colliderect(HatBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/HatSelect.png")
                if mouseHB.colliderect(SparePartsBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/SparePartSelect.png")
                if mouseHB.colliderect(EmotionBut):
                    GameplayBackground = pygame.image.load("Asset/RoomBackGround/EmotionSelect.png")
                
        screen.blit(pygame.transform.smoothscale(GameplayBackground, (widthSr, heightSr)), (0, 0))  # Fill with gameplay background
        screen.blit(pygame.transform.smoothscale(modelImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))  # Draw character frame
        
        screen.blit(pygame.transform.smoothscale(CameraButImage, (CameraBut.width + 25, CameraBut.height + 25)), (CameraBut.x - 15, CameraBut.y - 15))  # Draw camera button
        screen.blit(pygame.transform.smoothscale(HomeGameplayButImage, (HomeGameplayBut.width + 25, HomeGameplayBut.height + 25)), (HomeGameplayBut.x - 15, HomeGameplayBut.y - 15))
        
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