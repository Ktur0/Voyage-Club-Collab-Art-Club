import pygame
import webbrowser
import os
import time
import random

pygame.init()

# Đường dẫn tuyệt đối
BASE_DIR = os.path.dirname(__file__)  # thư mục chứa main.py
ASSET_DIR = os.path.join(BASE_DIR, "Asset")
SOUND_DIR = os.path.join(BASE_DIR, "Sound")
SAVE_PIC_DIR = os.path.join(BASE_DIR, "SavePicture")

# Set up screen
screenInfo = pygame.display.Info() 
pygame.display.set_caption("ACAN STYLE TOUR")
widthSr, heightSr = screenInfo.current_w - 200 , screenInfo.current_h
screen = pygame.display.set_mode((widthSr, heightSr), pygame.RESIZABLE)
currentScreen = "StartMenu"
run = True
yGameTitle = 500
# music = pygame.mixer.music.load("Sound/sound" + str(random.randint(1,2)) +".mp3")

# Setup âm thanh
music_on = True  # ban đầu đang bật nhạc
sound_files = [
    os.path.join(SOUND_DIR, "sound1.mp3"),
    os.path.join(SOUND_DIR, "sound2.mp3")
]
playlist = sound_files[:]  # copy danh sách gốc
random.shuffle(playlist)   # trộn thứ tự ban đầu
current_track = 0

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")
    except Exception as e:
        print(f"Failed to play {file_path}: {e}")

# Load assets
def load_asset(*path_parts):
    file_path = os.path.join(ASSET_DIR, *path_parts)
    if not os.path.exists(file_path):
        print(f"[ERROR] Missing asset: {file_path}")
        return pygame.Surface((100, 100))  # trả về ảnh trống thay vì crash
    return pygame.image.load(file_path)

play_music(playlist[current_track])  # Phát bài đầu tiên trong playlist

# Colors    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# Images for print screen
# Đầu chương trình
print_bg_files_no_logo = [
    load_asset("PrintBackGround", "halongbay1.png"),
    load_asset("PrintBackGround", "paris1.png"),
    load_asset("PrintBackGround", "pyramid1.png"),
    load_asset("PrintBackGround", "colosseum1.png"),
    load_asset("PrintBackGround", "bigben1.png")
]

print_bg_files = [
    load_asset("PrintBackGround", "halongbay.png"),
    load_asset("PrintBackGround", "paris.png"),
    load_asset("PrintBackGround", "pyramid.png"),
    load_asset("PrintBackGround", "colosseum.png"),
    load_asset("PrintBackGround", "bigben.png")
]

print_bg_index = 0
PrintBackground = print_bg_files[print_bg_index]
NextPrintButtonImage = load_asset("Button", "NextButton.png")
PreviousPrintButtonImage = load_asset("Button", "PreviousButton.png")
DownloadButtonImage = load_asset("Button", "DownloadButton.png")
HomePrintButtonImage = load_asset("Button", "HomeButton.png")
ReturnButtonImage = load_asset("Button", "PreviousButton.png")

# Images for gameplay screen
GameplayBackground = load_asset("RoomBackGround", "GameplayBackGround.png")
CameraButImage = load_asset("Button", "CameraButton.png")
HomeGameplayButImage = load_asset("Button", "HomeButton.png")
modelImage = load_asset("ACAN-MENU", "Model.png")
SelectionStore = ''
ShirtImage = ''
PaintImage = ''
ShoeImage = ''  
HatImage = ''
SparePartsImage = ''
EmotionImage = ''
GlassesImage = ''


# Story Frames
StoryImage1 = load_asset("COMIC", "1.png")
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
    global run
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseHB.colliderect(VoyageLogoBut):
                webbrowser.open("https://www.facebook.com/voyage.stc")
            if mouseHB.colliderect(ArtLogoBut):
                webbrowser.open("https://www.facebook.com/ArtclubTHD")
            if mouseHB.colliderect(QuitBut):
                run = False

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
        if event.type == MUSIC_END and music_on:
            current_track += 1
            if current_track >= len(playlist):
                random.shuffle(playlist)
                current_track = 0
            play_music(playlist[current_track])
  
    # Start menu logic
    if currentScreen == "StartMenu":

        if yGameTitle > 0:
            yGameTitle -= 50

        # Images for start screen
        StartMenuBackground = load_asset("ACAN-MENU", "StartMenu.png")
        StartButton = load_asset("Button", "StartButton.png")
        GameTitle = load_asset("ACAN-MENU", "GameTitle.png")

        # UI for start screen
        QuitBut = scale_rect(0.02, 0.027, 0.045, 0.08)
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        SoundBut = scale_rect(0.835, 0.027, 0.045, 0.08)
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
     
                if mouseHB.colliderect(SoundBut):
                    # Toggle sound on/off
                    music_on = not music_on
                    if music_on:
                        play_music(playlist[current_track])
                    else:
                        pygame.mixer.music.stop()
    
    elif currentScreen == "StoryMenu":

        # UI for story screen
        StoryMenuNextBut = scale_rect(0.91, 0.87, 0.07, 0.12)
        StoryFrame1 = scale_rect(0.036, 0.06, 0.44, 0.4)
        StoryFrame2 = scale_rect(0.52, 0.06, 0.44, 0.4)
        StoryFrame3 = scale_rect(0.036, 0.53, 0.44, 0.4)
        StoryFrame4 = scale_rect(0.52, 0.53, 0.44, 0.4)

        if int(time.time() - startTime) == 1:  # Show first image for 1 seconds
            StoryImage2 = load_asset("COMIC", "2.png")
        elif int(time.time() - startTime) == 2:  # Show second image for 2 seconds
            StoryImage3 = load_asset("COMIC", "3.png")
        elif int(time.time() - startTime) == 3:  # Show third image for 3 seconds
            StoryImage4 = load_asset("COMIC", "4.png")
        elif int(time.time() - startTime) == 4:  # Show fourth image for 4 seconds
            StoryMenuNextButtonImage = load_asset("Button","NextButton.png")  # Show next button

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
        QuitBut = scale_rect(0.02, 0.027, 0.045, 0.08)
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        SoundBut = scale_rect(0.835, 0.027, 0.045, 0.08)
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

        SelectButtons3x5 = [
            scale_rect(0.58, 0.19, 0.07, 0.11),
            scale_rect(0.7, 0.19, 0.07, 0.11),
            scale_rect(0.81, 0.19, 0.07, 0.11),

            scale_rect(0.58, 0.35, 0.07, 0.11),
            scale_rect(0.7, 0.35, 0.07, 0.11),
            scale_rect(0.81, 0.35, 0.07, 0.11),

            scale_rect(0.58, 0.5, 0.07, 0.11),
            scale_rect(0.7, 0.5, 0.07, 0.11),
            scale_rect(0.81, 0.5, 0.07, 0.11),

            scale_rect(0.58, 0.66, 0.07, 0.11),
            scale_rect(0.7, 0.66, 0.07, 0.11),
            scale_rect(0.81, 0.66, 0.07, 0.11),

            scale_rect(0.65, 0.81, 0.07, 0.11),
            scale_rect(0.77, 0.81, 0.07, 0.11)

        ]

        SelectButtons2x5 = [
            scale_rect(0.64, 0.19, 0.07, 0.11),
            scale_rect(0.76, 0.19, 0.07, 0.11),

            scale_rect(0.64, 0.35, 0.07, 0.11),
            scale_rect(0.76, 0.35, 0.07, 0.11),

            scale_rect(0.64, 0.5, 0.07, 0.11),
            scale_rect(0.76, 0.5, 0.07, 0.11),

            scale_rect(0.64, 0.66, 0.07, 0.11),
            scale_rect(0.76, 0.66, 0.07, 0.11),

            scale_rect(0.64, 0.81, 0.07, 0.11),
            scale_rect(0.76, 0.81, 0.07, 0.11)
        ]

        clickClubButton(events)  # Check if club buttons are clicked
        for event in events:

            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(CameraBut):
                    currentScreen = "PrintScreenMenu"
                
                if mouseHB.colliderect(HomeGameplayBut):
                    currentScreen = "StartMenu"
                
                if mouseHB.colliderect(SoundBut):
                    # Toggle sound on/off
                    music_on = not music_on
                    if music_on:
                        play_music(playlist[current_track])
                    else:
                        pygame.mixer.music.stop()

                
                if SelectionStore == 'Shirt':
                    for i in range(len(SelectButtons3x5)):
                        if mouseHB.colliderect(SelectButtons3x5[i]):
                            ShirtImage = load_asset("Top","top" + str(i + 1) + ".png")
                            break
                
                elif SelectionStore == 'Paint':
                    for i in range(len(SelectButtons3x5)):
                        if mouseHB.colliderect(SelectButtons3x5[i]):
                            PaintImage = load_asset( "Bottom", "bottom" + str(i + 1) + ".png")
                            break
                
                elif SelectionStore == 'Shoe':
                    for i in range(len(SelectButtons2x5)):
                        if mouseHB.colliderect(SelectButtons2x5[i]):
                            ShoeImage = load_asset("Shoe", "shoe" + str(i + 1) + ".png")
                            break
                
                elif SelectionStore == 'Hat':
                    for i in range(len(SelectButtons2x5)):
                        if mouseHB.colliderect(SelectButtons2x5[i]):
                            HatImage = load_asset("Hat", "hat" + str(i + 1) + ".png")
                            break
                
                elif SelectionStore == 'SpareParts':
                    for i in range(len(SelectButtons2x5)):
                        if mouseHB.colliderect(SelectButtons2x5[i]):
                            SparePartsImage = load_asset("SpareParts", "spareparts" + str(i + 1) + ".png")
                            break
                
                elif SelectionStore == 'Emotion':
                    for i in range(len(SelectButtons2x5)):
                        if i < 5:
                            if mouseHB.colliderect(SelectButtons2x5[i]):
                                EmotionImage = load_asset("Emotion", "emotion" + str(i + 1) + ".png")
                                break
                        else:
                            if mouseHB.colliderect(SelectButtons2x5[i]):
                                GlassesImage = load_asset("Emotion", "emotion" + str(i + 1) + ".png")
                                break

                if mouseHB.colliderect(ShirtBut):
                    GameplayBackground = load_asset("RoomBackGround", "ShirtSelect.png")
                    SelectionStore = 'Shirt'

                if mouseHB.colliderect(PaintBut):
                    GameplayBackground = load_asset("RoomBackGround", "PaintSelect.png")
                    SelectionStore = 'Paint'

                if mouseHB.colliderect(ShoeBut):
                    GameplayBackground = load_asset("RoomBackGround", "ShoeSelect.png")
                    SelectionStore = 'Shoe'

                if mouseHB.colliderect(HatBut):
                    GameplayBackground = load_asset("RoomBackGround", "HatSelect.png")
                    SelectionStore = 'Hat'

                if mouseHB.colliderect(SparePartsBut):
                    GameplayBackground = load_asset("RoomBackGround", "SparePartSelect.png")
                    SelectionStore = 'SpareParts'

                if mouseHB.colliderect(EmotionBut):
                    GameplayBackground = load_asset("RoomBackGround", "EmotionSelect.png")
                    SelectionStore = 'Emotion'
                
        screen.blit(pygame.transform.smoothscale(GameplayBackground, (widthSr, heightSr)), (0, 0))  # Fill with gameplay background
        screen.blit(pygame.transform.smoothscale(modelImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))  # Draw character frame
        # screen.blit(pygame.transform.smoothscale(CameraButImage, (CameraBut.width + 25, CameraBut.height + 25)), (CameraBut.x - 15, CameraBut.y - 15))  # Draw camera button
        # screen.blit(pygame.transform.smoothscale(HomeGameplayButImage, (HomeGameplayBut.width + 25, HomeGameplayBut.height + 25)), (HomeGameplayBut.x - 15, HomeGameplayBut.y - 15))
        
        if ShoeImage != '':
            screen.blit(pygame.transform.smoothscale(ShoeImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if PaintImage != '':
            screen.blit(pygame.transform.smoothscale(PaintImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if ShirtImage != '':
            screen.blit(pygame.transform.smoothscale(ShirtImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if EmotionImage != '':
            screen.blit(pygame.transform.smoothscale(EmotionImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if GlassesImage != '':
            screen.blit(pygame.transform.smoothscale(GlassesImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if HatImage != '':
            screen.blit(pygame.transform.smoothscale(HatImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if SparePartsImage != '':
            screen.blit(pygame.transform.smoothscale(SparePartsImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        
    elif currentScreen == "PrintScreenMenu":

        # UI for print screen menu
        QuitBut = scale_rect(0.02, 0.027, 0.045, 0.08)
        VoyageLogoBut = scale_rect(0.946, 0.027, 0.045, 0.08)
        ArtLogoBut = scale_rect(0.886, 0.027, 0.045, 0.08)
        SoundBut = scale_rect(0.835, 0.027, 0.045, 0.08)
        ReturnBut = scale_rect(0.02, 0.45, 0.07, 0.12)
        HomePrintBut = scale_rect(0.02, 0.61, 0.07, 0.12)
        NextPrintBut = scale_rect(0.925, 0.87, 0.055, 0.1)
        PreviousPrintBut = scale_rect(0.855, 0.87, 0.055, 0.1)
        DownloadBut = scale_rect(0.02, 0.28, 0.07, 0.12)
        CharacterFrame = scale_rect(0.36, 0.12, 0.36, 0.85)

        PrintBackground = print_bg_files[print_bg_index]

        # Check for button clicks
        clickClubButton(events)
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseHB.colliderect(DownloadBut):

                    PrintBackground = print_bg_files_no_logo[print_bg_index]

                    screen.blit(pygame.transform.smoothscale(PrintBackground, (widthSr, heightSr)), (0, 0))  # Fill with print background
                    screen.blit(pygame.transform.smoothscale(modelImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))  # Draw character frame

                    if ShoeImage != '':
                        screen.blit(pygame.transform.smoothscale(ShoeImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if PaintImage != '':
                        screen.blit(pygame.transform.smoothscale(PaintImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if ShirtImage != '':
                        screen.blit(pygame.transform.smoothscale(ShirtImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if EmotionImage != '':
                        screen.blit(pygame.transform.smoothscale(EmotionImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if GlassesImage != '':
                        screen.blit(pygame.transform.smoothscale(GlassesImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if HatImage != '':
                        screen.blit(pygame.transform.smoothscale(HatImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                    if SparePartsImage != '':
                        screen.blit(pygame.transform.smoothscale(SparePartsImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
                
                    subsurface = screen.subsurface((0,0, widthSr, heightSr)).copy() 
                    pygame.image.save(subsurface, "SavePicture/Screenshot"+str(countFilesInDirectory("SavePicture")) + ".png")

                if mouseHB.colliderect(ReturnBut):
                    currentScreen = "GameMenu"
                     
                if mouseHB.colliderect(HomePrintBut):
                    currentScreen = "StartMenu"

                if mouseHB.colliderect(SoundBut):
                    # Toggle sound on/off
                    music_on = not music_on
                    if music_on:
                        play_music(playlist[current_track])
                    else:
                        pygame.mixer.music.stop()


                # Khi bấm nút Next
                if mouseHB.colliderect(NextPrintBut):
                    if print_bg_index < len(print_bg_files) - 1:
                        print_bg_index += 1

                if mouseHB.colliderect(PreviousPrintBut):
                    if print_bg_index > 0:
                        print_bg_index -= 1

        # Print screen logic can go here
        screen.blit(pygame.transform.smoothscale(PrintBackground, (widthSr, heightSr)), (0, 0))  # Fill with print background

        # Draw buttons
        screen.blit(pygame.transform.smoothscale(DownloadButtonImage, (DownloadBut.width + 25, DownloadBut.height + 25)), (DownloadBut.x - 13, DownloadBut.y - 12))  # Draw download button
        screen.blit(pygame.transform.smoothscale(HomePrintButtonImage, (HomePrintBut.width + 25, HomePrintBut.height + 25)), (HomePrintBut.x - 13, HomePrintBut.y - 12))  # Draw home print button
        screen.blit(pygame.transform.smoothscale(ReturnButtonImage, (ReturnBut.width + 25, ReturnBut.height + 25)), (ReturnBut.x - 13, ReturnBut.y - 12))
        screen.blit(pygame.transform.smoothscale(NextPrintButtonImage, (NextPrintBut.width + 20, NextPrintBut.height + 20)), (NextPrintBut.x - 12, NextPrintBut.y - 12))  # Draw next print button
        screen.blit(pygame.transform.smoothscale(PreviousPrintButtonImage, (PreviousPrintBut.width + 20, PreviousPrintBut.height + 20)), (PreviousPrintBut.x - 12, PreviousPrintBut.y - 12))  # Draw previous print button  
        screen.blit(pygame.transform.smoothscale(modelImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))  # Draw character frame

        if ShoeImage != '':
            screen.blit(pygame.transform.smoothscale(ShoeImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if PaintImage != '':
            screen.blit(pygame.transform.smoothscale(PaintImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if ShirtImage != '':
            screen.blit(pygame.transform.smoothscale(ShirtImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if EmotionImage != '':
            screen.blit(pygame.transform.smoothscale(EmotionImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if GlassesImage != '':
            screen.blit(pygame.transform.smoothscale(GlassesImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if HatImage != '':
            screen.blit(pygame.transform.smoothscale(HatImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
        if SparePartsImage != '':
            screen.blit(pygame.transform.smoothscale(SparePartsImage, (CharacterFrame.width, CharacterFrame.height)), (CharacterFrame.x, CharacterFrame.y))
    
    # Update screen
    pygame.display.update()
    
pygame.quit()
