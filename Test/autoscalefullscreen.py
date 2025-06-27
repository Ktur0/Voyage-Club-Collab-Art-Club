import pygame
import webbrowser
import os

pygame.init()

# Set up screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

def scale_rect(xr, yr, wr, hr):
    return pygame.Rect(int(xr* screen_width), int(yr * screen_height), int(wr * screen_width), int(hr * screen_height))

def update_buttons():
    global VoyageLogoBut, ArtLogoBut, StartBut, StoryMenuNextBut
    global CameraBut, HomeGameplayBut, ShirtBut, PaintBut, ShoeBut
    global HatBut, SparePartsBut, EmotionBut, DownloadBut, ReturnBut
    global HomePrintBut, NextPrintBut, PreviousPrintBut
    global StoryFrame1, StoryFrame2, StoryFrame3, StoryFrame4
    global CharacterFrame, ItemFrame, PhotoFrame

    VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
    ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
    StartBut = scale_rect(0.45, 0.72, 0.1, 0.18)
    StoryMenuNextBut = scale_rect(0.91, 0.84, 0.07, 0.12)
    CameraBut = scale_rect(0.02, 0.36, 0.07, 0.12)
    HomeGameplayBut = scale_rect(0.02, 0.52, 0.07, 0.12)
    ShirtBut = scale_rect(0.89, 0.17, 0.06, 0.1)
    PaintBut = scale_rect(0.89, 0.30, 0.06, 0.1)
    ShoeBut = scale_rect(0.89, 0.43, 0.06, 0.1)
    HatBut = scale_rect(0.89, 0.56, 0.06, 0.1)
    SparePartsBut = scale_rect(0.89, 0.69, 0.06, 0.1)
    EmotionBut = scale_rect(0.89, 0.82, 0.06, 0.1)
    DownloadBut = scale_rect(0.02, 0.28, 0.07, 0.12)
    ReturnBut = scale_rect(0.02, 0.45, 0.07, 0.12)
    HomePrintBut = scale_rect(0.02, 0.61, 0.07, 0.12)
    NextPrintBut = scale_rect(0.925, 0.87, 0.055, 0.1)
    PreviousPrintBut = scale_rect(0.855, 0.87, 0.055, 0.1)

    StoryFrame1 = scale_rect(0.036, 0.06, 0.44, 0.4)
    StoryFrame2 = scale_rect(0.52, 0.06, 0.44, 0.4)
    StoryFrame3 = scale_rect(0.036, 0.53, 0.44, 0.4)
    StoryFrame4 = scale_rect(0.52, 0.53, 0.44, 0.4)

    CharacterFrame = scale_rect(0.13, 0.09, 0.36, 0.85)
    ItemFrame = scale_rect(0.54, 0.14, 0.38, 0.78)

    PhotoFrame = scale_rect(0.32, 0.09, 0.36, 0.85)

update_buttons()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# Mouse
mouseSize = 20
mouseHB = pygame.Rect(0, 0, mouseSize, mouseSize)

# Screen states
StrMenuScr = True
StoryMenuScr = False
GameMenuScr = False
PrintScrMenuScr = False

def clickClubButton(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseHB.colliderect(VoyageLogoBut):
                webbrowser.open("https://www.facebook.com/voyage.stc")
            if mouseHB.colliderect(ArtLogoBut):
                webbrowser.open("https://www.facebook.com/ArtclubTHD")

def countFilesInDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# Main loop
run = True
while run:
    # Update resolution if screen changed (resize or rotation)
    new_w, new_h = screen.get_size()
    if (new_w != screen_width or new_h != screen_height):
        screen_width, screen_height = new_w, new_h
        update_buttons()

    # Update mouse
    xMouse, yMouse = pygame.mouse.get_pos()
    mouseHB.topleft = (xMouse, yMouse)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if StrMenuScr:
        screen.fill(WHITE)
        clickClubButton(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(StartBut):
                    StrMenuScr = False
                    StoryMenuScr = True

        pygame.draw.circle(screen, RED, VoyageLogoBut.center, VoyageLogoBut.width // 2)
        pygame.draw.circle(screen, YELLOW, ArtLogoBut.center, ArtLogoBut.width // 2)
        pygame.draw.circle(screen, GREY, StartBut.center, StartBut.width // 2)

    elif StoryMenuScr:
        screen.fill(WHITE)
        clickClubButton(events)
    
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(StoryMenuNextBut):
                    StoryMenuScr = False
                    GameMenuScr = True

        for frame in [StoryFrame1, StoryFrame2, StoryFrame3, StoryFrame4]:
            pygame.draw.rect(screen, GREY, frame)

        pygame.draw.circle(screen, RED, StoryMenuNextBut.center, StoryMenuNextBut.width // 2)

    elif GameMenuScr:
        screen.fill(WHITE)
        clickClubButton(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(CameraBut):
                    GameMenuScr = False
                    PrintScrMenuScr = True
                elif mouseHB.colliderect(HomeGameplayBut):
                    GameMenuScr = False
                    StrMenuScr = True

        pygame.draw.rect(screen, BLUE, CharacterFrame)
        pygame.draw.rect(screen, RED, ItemFrame)

        for btn, color in [
            (VoyageLogoBut, RED), (ArtLogoBut, YELLOW),
            (CameraBut, GREEN), (HomeGameplayBut, YELLOW),
            (ShirtBut, GREY), (PaintBut, GREY), (ShoeBut, GREY),
            (HatBut, GREY), (SparePartsBut, GREY), (EmotionBut, GREY)
        ]:
            pygame.draw.circle(screen, color, btn.center, btn.width // 2)

    elif PrintScrMenuScr:
        screen.fill(WHITE)
        clickClubButton(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(DownloadBut):
                    subsurface = screen.subsurface(PhotoFrame).copy()
                    filename = f"SavePicture/Screenshot{countFilesInDirectory('SavePicture')}.png"
                    pygame.image.save(subsurface, filename)

                elif mouseHB.colliderect(ReturnBut):
                    PrintScrMenuScr = False
                    GameMenuScr = True

                elif mouseHB.colliderect(HomePrintBut):
                    PrintScrMenuScr = False
                    StrMenuScr = True

        pygame.draw.rect(screen, GREY, PhotoFrame)

        for btn, color in [
            (VoyageLogoBut, RED), (ArtLogoBut, YELLOW),
            (DownloadBut, GREEN), (ReturnBut, YELLOW),
            (HomePrintBut, GREY), (NextPrintBut, GREY), (PreviousPrintBut, GREY)
        ]:
            pygame.draw.circle(screen, color, btn.center, btn.width // 2)

    pygame.display.update()

pygame.quit()
