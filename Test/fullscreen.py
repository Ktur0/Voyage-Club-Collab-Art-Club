import pygame
import sys

pygame.init()

# Kích thước gốc (base resolution)
BASE_WIDTH, BASE_HEIGHT = 800, 600
screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Window with Scaling")

# Các element cần scale
class Button:
    def __init__(self, x, y, width, height, text):
        self.original_rect = pygame.Rect(x, y, width, height)
        self.rect = self.original_rect.copy()
        self.text = text
        self.color = (100, 200, 100)
    
    def draw(self, surface, scale_x, scale_y):
        # Tính toán kích thước và vị trí mới
        self.rect.x = int(self.original_rect.x * scale_x)
        self.rect.y = int(self.original_rect.y * scale_y)
        self.rect.width = int(self.original_rect.width * scale_x)
        self.rect.height = int(self.original_rect.height * scale_y)
        
        pygame.draw.rect(surface, self.color, self.rect)
        font_size = int(24 * min(scale_x, scale_y))
        font = pygame.font.SysFont('Arial', font_size)
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

# Tạo các element
button = Button(300, 250, 200, 80, "Click Me!")
circle_pos = (400, 400)
circle_radius = 50

running = True
while running:
    current_width, current_height = screen.get_size()
    scale_x = current_width / BASE_WIDTH
    scale_y = current_height / BASE_HEIGHT
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.VIDEORESIZE:
            # Khi cửa sổ thay đổi kích thước
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                # Toggle fullscreen
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
                else:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Vẽ
    screen.fill((240, 240, 240))
    
    # Vẽ button với scaling
    button.draw(screen, scale_x, scale_y)
    
    # Vẽ circle với scaling
    scaled_circle_pos = (int(circle_pos[0] * scale_x), int(circle_pos[1] * scale_y))
    scaled_radius = int(circle_radius * min(scale_x, scale_y))
    pygame.draw.circle(screen, (200, 100, 100), scaled_circle_pos, scaled_radius)
    
    pygame.display.flip()

pygame.quit()
sys.exit()