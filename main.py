import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Конвертер RUB -> USD")

counter = 0

font = pygame.font.Font(None, 48)

# Кнопка Конвертировать
convert_button = pygame.Rect(screen_width//8, screen_width*3//8, screen_width//4, screen_width//8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()