import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
ship = pygame.Rect(400,500,50,30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.x -= 5
    if keys[pygame.K_RIGHT]:
        ship.x += 5
    
    screen.fill((135,206,235))  # 空色
    pygame.draw.rect(screen, (255,0,0), ship)  # スカイシップ
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
