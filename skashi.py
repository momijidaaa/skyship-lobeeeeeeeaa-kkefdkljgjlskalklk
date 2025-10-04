import pygame

# Pygame 初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SkyShip Game")
clock = pygame.time.Clock()

# 船の設定
ship_width, ship_height = 50, 30
ship_speed = 5
ship = pygame.Rect(400, 500, ship_width, ship_height)

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship.x += ship_speed

    # 画面端で止まる
    if ship.x < 0:
        ship.x = 0
    if ship.x + ship.width > SCREEN_WIDTH:
        ship.x = SCREEN_WIDTH - ship.width

    # 描画
    screen.fill((135, 206, 235))  # 空色
    pygame.draw.rect(screen, (255, 0, 0), ship)  # 船
    pygame.display.flip()

    clock.tick(60)  # 60FPS

pygame.quit()
