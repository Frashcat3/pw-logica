import pygame
pygame.init()
LARGURA = 850
ALTURA = 650
tela = pygame.display.set_mode(
    (LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders")  
FUNDO = (0, 0, 0)  
VERDE = (100, 255, 100)
TAMANHO_PIXEL = 50
alien = [
    "111111111111111",
    "100001000100001",
    "100000111000001",
    "100011111110001",
    "100111010111001",
    "100101111101001",
    "100101000101001",
    "100000101000001",
    "100000000000001",
    "111111111111111",    
]
inicio_x = 50
inicio_y = 50
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((FUNDO))
    for linha in range(len(alien)):
        for coluna in range (len(alien[linha])):
            if alien[linha][coluna] == "1":
                x = inicio_x + coluna * TAMANHO_PIXEL
                y = inicio_y + linha * TAMANHO_PIXEL
                pygame.draw.rect(
                    tela,
                    VERDE,
                    (x, y, TAMANHO_PIXEL - 2, TAMANHO_PIXEL - 2,)
                )    
    pygame.display.update()
pygame.quit()

