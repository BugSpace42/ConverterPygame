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
font_digits = pygame.font.Font(None, 80)

# Поле для рублей
rubles_rect = pygame.Rect(screen_width * 4 // 9, screen_width // 9, screen_width * 4 // 9, screen_width // 6)
# Поле для курса
rate_rect = pygame.Rect(screen_width * 4 // 9, screen_width * 5 // 9, screen_width * 4 // 9, screen_width // 6)
# Кнопка конвертации
button_rect = pygame.Rect(screen_width * 2 // 9, screen_width * 3 // 9, screen_width * 5 // 9, screen_width // 6)

# Данные
rubles_text = ""  # Текст в поле рублей
rate_text = "90"  # Текст в поле курса (начальный курс 90)
active_field = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Проверяем, куда кликнули
            if rubles_rect.collidepoint(mouse_pos):
                active_field = "rubles"
            elif rate_rect.collidepoint(mouse_pos):
                active_field = "rate"
            else:
                active_field = None

            # Обработка нажатия клавиш
        elif event.type == pygame.KEYDOWN:
            if active_field == "rubles":
                if event.key == pygame.K_BACKSPACE:
                    rubles_text = rubles_text[:-1]  # Удаляем последний символ
                else:
                    # Добавляем только цифры или точку
                    if event.unicode.isdigit() or event.unicode == ".":
                        rubles_text += event.unicode

            elif active_field == "rate":
                if event.key == pygame.K_BACKSPACE:
                    rate_text = rate_text[:-1]
                else:
                    if event.unicode.isdigit() or event.unicode == ".":
                        rate_text += event.unicode

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

    rubles_display = font_digits.render(rubles_text if rubles_text else "0", True, WHITE)
    screen.blit(rubles_display, (rubles_rect.x + 15, rubles_rect.y + 20))

    rate_display = font_digits.render(rate_text, True, WHITE)
    screen.blit(rate_display, (rate_rect.x + 15, rate_rect.y + 20))

    pygame.display.flip()

pygame.quit()