import pygame

pygame.init()

screen = pygame.display.set_mode([1280,719])
# screen.fill('blue')

pygame.display.flip()

velocidade = 5
rosa ='pink'
l = 20
a = 25
x = 250
y = 250

pygame.display.set_caption('TITULO')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas [pygame.K_RIGHT]:
        x += velocidade 

    screen.fill('blue')
    pygame.draw.rect(screen,rosa,(x,y,l,a))
    pygame.display.flip()
    pygame.time.Clock().tick(30)