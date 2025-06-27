# Thêm ngay sau import
import pygame
import webbrowser
import os

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w - 100, infoObject.current_h - 100), pygame.RESIZABLE)
pygame.display.set_caption("Voyage Club - Art Club")
clock = pygame.time.Clock()
run = True

# === Tooltip Font ===
font_path = os.path.join("Font", "ARIAL.TTF")  # đổi "myfont.ttf" đúng tên file
font = pygame.font.Font(font_path, 24)


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

# Flags
StrMenuScr = True
StoryMenuScr = False
GameMenuScr = False
PrintScrMenuScr = False

def rel_rect(x, y, w, h, sw, sh):
    return pygame.Rect(int(x * sw), int(y * sh), int(w * sw), int(h * sh))

def countFilesInDirectory(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def draw_circle_rect(screen, color, rect):
    pygame.draw.circle(screen, color, rect.center, rect.width // 2)

def clickClubButton(mouseHB, VoyageLogoBut, ArtLogoBut):
    if mouseHB.colliderect(VoyageLogoBut):
        webbrowser.open("https://www.facebook.com/voyage.stc")
    if mouseHB.colliderect(ArtLogoBut):
        webbrowser.open("https://www.facebook.com/ArtclubTHD")

def draw_tooltip(text, pos):
    surf = font.render(text, True, (0, 0, 0))
    rect = surf.get_rect(topleft=(pos[0] + 10, pos[1] + 10))
    bg_rect = pygame.Rect(rect.x - 4, rect.y - 2, rect.width + 8, rect.height + 4)
    pygame.draw.rect(screen, (255, 255, 200), bg_rect)
    pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
    screen.blit(surf, rect)

while run:
    screen.fill(WHITE)
    sw, sh = screen.get_size()
    events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouseHB = pygame.Rect(mouse_x, mouse_y, 1, 1)
    tooltip_text = None

    # UI Elements
    VoyageLogoBut = rel_rect(0.95, 0.03, 0.045, 0.075, sw, sh)
    ArtLogoBut = rel_rect(0.885, 0.03, 0.045, 0.075, sw, sh)
    StartBut = rel_rect(0.45, 0.72, 0.1, 0.15, sw, sh)
    StoryMenuNextBut = rel_rect(0.91, 0.84, 0.07, 0.12, sw, sh)
    StoryFrame1 = rel_rect(0.035, 0.065, 0.44, 0.36, sw, sh)
    StoryFrame2 = rel_rect(0.52, 0.065, 0.44, 0.36, sw, sh)
    StoryFrame3 = rel_rect(0.035, 0.55, 0.44, 0.36, sw, sh)
    StoryFrame4 = rel_rect(0.52, 0.55, 0.44, 0.36, sw, sh)
    CameraBut = rel_rect(0.02, 0.35, 0.07, 0.12, sw, sh)
    HomeGameplayBut = rel_rect(0.02, 0.52, 0.07, 0.12, sw, sh)
    CharacterFrame = rel_rect(0.13, 0.08, 0.35, 0.85, sw, sh)
    ItemFrame = rel_rect(0.55, 0.15, 0.37, 0.75, sw, sh)
    DownloadBut = rel_rect(0.02, 0.27, 0.07, 0.12, sw, sh)
    ReturnBut = rel_rect(0.02, 0.43, 0.07, 0.12, sw, sh)
    HomePrintBut = rel_rect(0.02, 0.59, 0.07, 0.12, sw, sh)
    NextPrintBut = rel_rect(0.925, 0.87, 0.055, 0.09, sw, sh)
    PreviousPrintBut = rel_rect(0.85, 0.87, 0.055, 0.09, sw, sh)
    PhotoFrame = rel_rect(0.32, 0.08, 0.35, 0.85, sw, sh)

    # UI Drawing
    if StrMenuScr:
        draw_circle_rect(screen, RED, VoyageLogoBut)
        draw_circle_rect(screen, YELLOW, ArtLogoBut)
        draw_circle_rect(screen, GREY, StartBut)
        if mouseHB.colliderect(StartBut):
            tooltip_text = "Bắt đầu"
    elif StoryMenuScr:
        pygame.draw.rect(screen, GREY, StoryFrame1)
        pygame.draw.rect(screen, GREY, StoryFrame2)
        pygame.draw.rect(screen, GREY, StoryFrame3)
        pygame.draw.rect(screen, GREY, StoryFrame4)
        draw_circle_rect(screen, RED, StoryMenuNextBut)
        draw_circle_rect(screen, RED, VoyageLogoBut)
        draw_circle_rect(screen, YELLOW, ArtLogoBut)
        if mouseHB.colliderect(StoryMenuNextBut):
            tooltip_text = "Tiếp theo"
    elif GameMenuScr:
        pygame.draw.rect(screen, BLUE, CharacterFrame)
        pygame.draw.rect(screen, RED, ItemFrame)
        draw_circle_rect(screen, RED, VoyageLogoBut)
        draw_circle_rect(screen, YELLOW, ArtLogoBut)
        draw_circle_rect(screen, GREEN, CameraBut)
        draw_circle_rect(screen, YELLOW, HomeGameplayBut)
        if mouseHB.colliderect(CameraBut):
            tooltip_text = "Chụp ảnh"
        elif mouseHB.colliderect(HomeGameplayBut):
            tooltip_text = "Trang chính"
    elif PrintScrMenuScr:
        pygame.draw.rect(screen, GREY, PhotoFrame)
        draw_circle_rect(screen, RED, VoyageLogoBut)
        draw_circle_rect(screen, YELLOW, ArtLogoBut)
        draw_circle_rect(screen, GREEN, DownloadBut)
        draw_circle_rect(screen, YELLOW, ReturnBut)
        draw_circle_rect(screen, GREY, HomePrintBut)
        draw_circle_rect(screen, GREY, NextPrintBut)
        draw_circle_rect(screen, GREY, PreviousPrintBut)
        if mouseHB.colliderect(DownloadBut):
            tooltip_text = "Lưu ảnh"
        elif mouseHB.colliderect(ReturnBut):
            tooltip_text = "Quay lại"
        elif mouseHB.colliderect(HomePrintBut):
            tooltip_text = "Trang chính"
        elif mouseHB.colliderect(NextPrintBut):
            tooltip_text = "Trang kế"
        elif mouseHB.colliderect(PreviousPrintBut):
            tooltip_text = "Trang trước"

    # Tooltip chung cho logo
    if mouseHB.colliderect(VoyageLogoBut):
        tooltip_text = "Facebook Voyage Club"
    elif mouseHB.colliderect(ArtLogoBut):
        tooltip_text = "Facebook Art Club"

    for event in events:
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickClubButton(mouseHB, VoyageLogoBut, ArtLogoBut)

            if StrMenuScr and mouseHB.colliderect(StartBut):
                pygame.display.update()
                pygame.time.delay(200)
                StrMenuScr = False
                StoryMenuScr = True

            elif StoryMenuScr and mouseHB.colliderect(StoryMenuNextBut):
                pygame.display.update()
                pygame.time.delay(200)
                StoryMenuScr = False
                GameMenuScr = True

            elif GameMenuScr:
                if mouseHB.colliderect(CameraBut):
                    pygame.display.update()
                    pygame.time.delay(200)
                    GameMenuScr = False
                    PrintScrMenuScr = True
                elif mouseHB.colliderect(HomeGameplayBut):
                    pygame.display.update()
                    pygame.time.delay(200)
                    GameMenuScr = False
                    StrMenuScr = True

            elif PrintScrMenuScr:
                if mouseHB.colliderect(DownloadBut):
                    subsurface = screen.subsurface(PhotoFrame).copy()
                    if not os.path.exists("SavePicture"):
                        os.makedirs("SavePicture")
                    filename = "SavePicture/Screenshot" + str(countFilesInDirectory("SavePicture")) + ".png"
                    pygame.image.save(subsurface, filename)
                elif mouseHB.colliderect(ReturnBut):
                    pygame.display.update()
                    pygame.time.delay(200)
                    PrintScrMenuScr = False
                    GameMenuScr = True
                elif mouseHB.colliderect(HomePrintBut):
                    pygame.display.update()
                    pygame.time.delay(200)
                    PrintScrMenuScr = False
                    StrMenuScr = True

    # Vẽ tooltip nếu có
    if tooltip_text:
        draw_tooltip(tooltip_text, (mouse_x, mouse_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
