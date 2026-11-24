import pygame
import random
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela
LARGURA = 850
ALTURA = 650
TAMANHO_BLOCO = 30

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake - Python")

# Cores RGB
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Relógio e fonte
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 25)

# Posição inicial da cobrinha
cobra = [
    [100, 100],
    [80, 100],
    [60, 100]
]

# Direção inicial
direcao = "DIREITA"

# Gerar comida
comida = [
    random.randrange(0, LARGURA, TAMANHO_BLOCO),
    random.randrange(0, ALTURA, TAMANHO_BLOCO)
]

# Pontuação
pontos = 0

# Loop principal
rodando = True

while rodando:

    # Capturar eventos do teclado
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_UP and direcao != "BAIXO":
                direcao = "CIMA"

            elif evento.key == pygame.K_DOWN and direcao != "CIMA":
                direcao = "BAIXO"

            elif evento.key == pygame.K_LEFT and direcao != "DIREITA":
                direcao = "ESQUERDA"

            elif evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                direcao = "DIREITA"

    # Movimentar a cabeça da cobrinha
    cabeca = cobra[0].copy()

    if direcao == "CIMA":
        cabeca[1] -= TAMANHO_BLOCO

    elif direcao == "BAIXO":
        cabeca[1] += TAMANHO_BLOCO

    elif direcao == "ESQUERDA":
        cabeca[0] -= TAMANHO_BLOCO

    elif direcao == "DIREITA":
        cabeca[0] += TAMANHO_BLOCO

    # Adicionar nova cabeça
    cobra.insert(0, cabeca)

    # Verificar se comeu
    if cabeca == comida:
        pontos += 1

        while comida in cobra:
            comida = [
                random.randrange(0, LARGURA, TAMANHO_BLOCO),
                random.randrange(0, ALTURA, TAMANHO_BLOCO)
            ]
    else:
        # Remover a cauda para manter o tamanho
        cobra.pop()

    # Verificar colisões
    if (
        cabeca[0] < 0 or
        cabeca[0] >= LARGURA or
        cabeca[1] < 0 or
        cabeca[1] >= ALTURA or
        cabeca in cobra[1:]
    ):
        rodando = False

    # Desenhar elementos
    tela.fill(PRETO)

    # Desenhar cobrinha
    for parte in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            (parte[0], parte[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

    # Desenhar comida
    pygame.draw.rect(
        tela,
        VERMELHO,
        (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
    )

    # Mostrar pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

    # Atualizar a tela
    pygame.display.update()

    # Controlar velocidade
    relogio.tick(10)

# Tela de Game Over
tela.fill(PRETO)

mensagem = fonte.render("GAME OVER!", True, VERMELHO)
resultado = fonte.render(f"Pontuacao: {pontos}", True, BRANCO)

tela.blit(mensagem, (220, 150))
tela.blit(resultado, (220, 190))

pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
sys.exit()