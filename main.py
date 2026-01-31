import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Конвертер RUB -> USD")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
BLUE = (70, 130, 180)
GREEN = (60, 179, 113)
RED = (220, 20, 60)

font = pygame.font.Font(None, 40)

# Поле для рублей
rubles_rect = pygame.Rect(screen_width * 4 // 9, screen_width // 9, screen_width * 4 // 9, screen_width // 6)
# Поле для курса
rate_rect = pygame.Rect(screen_width * 4 // 9, screen_width * 5 // 9, screen_width * 4 // 9, screen_width // 6)
# Кнопка конвертации
button_rect = pygame.Rect(screen_width * 2 // 9, screen_width * 3 // 9, screen_width * 5 // 9, screen_width // 6)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    # Рисуем поля ввода
    pygame.draw.rect(screen, BLACK, rubles_rect)
    pygame.draw.rect(screen, WHITE, rubles_rect, 2)

    pygame.draw.rect(screen, BLACK, rate_rect)
    pygame.draw.rect(screen, WHITE, rate_rect, 2)

    # Рисуем кнопку
    pygame.draw.rect(screen, (0, 100, 200), button_rect)

    # Метка для рублей
    rubles_label = font.render("Рубли:", True, WHITE)
    screen.blit(rubles_label, (screen_width // 9, screen_width // 9 + 30))

    # Метка для курса
    rate_label = font.render("Курс:", True, WHITE)
    screen.blit(rate_label, (screen_width // 9, screen_width * 5 // 9 + 30))

    # Текст на кнопке
    button_text = font.render("Конвертировать", True, WHITE)
    screen.blit(button_text, (screen_width * 2 // 9 + 55, screen_width * 3 // 9 + 35))

    pygame.display.flip()

pygame.quit()