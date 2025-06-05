import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chụp vùng màn hình")

# Vẽ thử cái gì đó lên màn hình
screen.fill((255, 255, 255))  # Nền trắng
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))  # Hình chữ nhật đỏ

pygame.display.flip()  # Cập nhật màn hình

# Chụp vùng (100, 100, 200, 150)
rect = pygame.Rect(100, 100, 200, 150)
subsurface = screen.subsurface(rect).copy()  # Copy để không bị phụ thuộc màn hình gốc

# Lưu ảnh
pygame.image.save(subsurface, "vung_chup.png")
print("Đã lưu ảnh thành công!")

# Thoát sau vài giây (tuỳ bạn)
pygame.time.wait(2000)
pygame.quit()
