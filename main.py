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
font_result = pygame.font.Font(None, 60)

# Поле для рублей
rubles_rect = pygame.Rect(screen_width * 4 // 9, screen_width // 9, screen_width * 4 // 9, screen_width // 6)
# Поле для курса
rate_rect = pygame.Rect(screen_width * 4 // 9, screen_width * 5 // 9, screen_width * 4 // 9, screen_width // 6)
# Кнопка конвертации
button_rect = pygame.Rect(screen_width * 2 // 9, screen_width * 3 // 9, screen_width * 5 // 9, screen_width // 6)
# Поле для результата
result_rect = pygame.Rect(screen_width // 9, screen_width * 8 // 9 - 80, screen_width * 7 // 9, 80)

# Данные
rubles_text = ""  # Текст в поле рублей
rate_text = "90"  # Текст в поле курса (начальный курс 90)
active_field = None
result_text = "0.00 USD"  # Результат конвертации

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

            # Проверяем, нажали ли на кнопку конвертации
            if button_rect.collidepoint(mouse_pos):
                try:
                    # Преобразуем текст в числа
                    rubles = float(rubles_text) if rubles_text else 0
                    rate = float(rate_text) if rate_text else 90

                    # Проверяем, что курс больше 0
                    if rate > 0:
                        # Вычисляем результат
                        dollars = rubles / rate
                        # Форматируем с 2 знаками после запятой
                        result_text = f"{dollars:.2f} USD"
                    else:
                        result_text = "Ошибка: курс 0"
                except:
                    result_text = "Ошибка ввода"

        # Обработка нажатия клавиш
        elif event.type == pygame.KEYDOWN:
            if active_field == "rubles":
                if event.key == pygame.K_BACKSPACE:
                    rubles_text = rubles_text[:-1]  # Удаляем последний символ
                elif event.key == pygame.K_RETURN:  # Конвертация по нажатию Enter
                    try:
                        rubles = float(rubles_text) if rubles_text else 0
                        rate = float(rate_text) if rate_text else 90
                        if rate > 0:
                            dollars = rubles / rate
                            result_text = f"{dollars:.2f} USD"
                        else:
                            result_text = "Ошибка: курс 0"
                    except:
                        result_text = "Ошибка ввода"
                else:
                    # Добавляем только цифры или точку
                    if event.unicode.isdigit() or event.unicode == ".":
                        # Ограничиваем длину ввода
                        if len(rubles_text) < 10:
                            rubles_text += event.unicode

            elif active_field == "rate":
                if event.key == pygame.K_BACKSPACE:
                    rate_text = rate_text[:-1]
                elif event.key == pygame.K_RETURN:  # Обновление курса по Enter
                    try:
                        new_rate = float(rate_text)
                        if new_rate > 0:
                            # Автоматически пересчитываем результат
                            rubles = float(rubles_text) if rubles_text else 0
                            dollars = rubles / new_rate
                            result_text = f"{dollars:.2f} USD"
                        else:
                            result_text = "Ошибка: курс 0"
                    except:
                        pass  # Если ошибка, оставляем старый курс
                else:
                    if event.unicode.isdigit() or event.unicode == ".":
                        # Ограничиваем длину ввода
                        if len(rate_text) < 8:
                            rate_text += event.unicode

    screen.fill(BLACK)

    # Рисуем поля ввода с разными цветами рамок для активного поля
    rubles_border_color = GREEN if active_field == "rubles" else WHITE
    rate_border_color = GREEN if active_field == "rate" else WHITE

    pygame.draw.rect(screen, BLACK, rubles_rect)
    pygame.draw.rect(screen, rubles_border_color, rubles_rect, 3)

    pygame.draw.rect(screen, BLACK, rate_rect)
    pygame.draw.rect(screen, rate_border_color, rate_rect, 3)

    # Рисуем кнопку
    pygame.draw.rect(screen, BLUE, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)

    # Рисуем поле результата
    pygame.draw.rect(screen, (30, 30, 30), result_rect)
    pygame.draw.rect(screen, GREEN, result_rect, 3)

    # Метка для рублей
    rubles_label = font.render("Рубли:", True, WHITE)
    screen.blit(rubles_label, (screen_width // 9, screen_width // 9 + 30))

    # Метка для курса
    rate_label = font.render("Курс:", True, WHITE)
    screen.blit(rate_label, (screen_width // 9, screen_width * 5 // 9 + 30))

    # Текст на кнопке
    button_text = font.render("Конвертировать", True, WHITE)
    screen.blit(button_text, (screen_width * 2 // 9 + 55, screen_width * 3 // 9 + 35))

    # Введенный текст в полях
    rubles_display = font_digits.render(rubles_text if rubles_text else "0", True, WHITE)
    screen.blit(rubles_display, (rubles_rect.x + 15, rubles_rect.y + 20))

    rate_display = font_digits.render(rate_text, True, WHITE)
    screen.blit(rate_display, (rate_rect.x + 15, rate_rect.y + 20))

    # Результат
    result_display = font_result.render(result_text, True, GREEN)
    result_x = result_rect.x + (result_rect.width - result_display.get_width()) // 2
    result_y = result_rect.y + (result_rect.height - result_display.get_height()) // 2
    screen.blit(result_display, (result_x, result_y))

    pygame.display.flip()

pygame.quit()