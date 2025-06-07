import pygame
import webbrowser
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Nút mở trang web")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 122, 255)
DARK_BLUE = (0, 100, 200)

# Font chữ
font = pygame.font.SysFont(None, 36)

# Tạo nút (rect và text)
button_rect = pygame.Rect(120, 120, 160, 50)
button_text = font.render("Mở Web", True, WHITE)

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Lấy vị trí chuột
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Kiểm tra nếu chuột đang hover nút
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, DARK_BLUE, button_rect)
        if mouse_pressed[0]:  # Nếu nhấn chuột trái
            webbrowser.open("https://www.google.com")  # 👉 Thay URL tại đây
            pygame.time.delay(300)  # Đợi một chút để tránh mở nhiều lần
    else:
        pygame.draw.rect(screen, BLUE, button_rect)

    # Vẽ chữ lên nút
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    # Xử lý sự kiện đóng cửa sổ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
