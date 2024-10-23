import pygame
import random
import time

#inicializando
pygame.init

#cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

#definiçoes da tela
largura_tela = 700
altura_tela = 400
tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('jogo da cobrinha')

#definiçoes da cobra
tamanho_celula = 10
velocidade = 12
clock = pygame.time.Clock()

#fontes
fonte = pygame.font.SysFont("arial", 25)

#funçao de pontuaçao
def pontuacao(score):
    valor = fonte.render("pontuação: ") + str(score), True, branco
    tela.blit(valor, [0,0])

#funçao desenhar a cobra
def cobra(tamanho_celula, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_celula, tamanho_celula])

#funçao principal
def jogo():
    #posicoes iniciais da cobra
    x_cobra = altura_tela / 2
    y_cobra = largura_tela / 2

    #movimento inicial
    x_mudanca = 0
    y_mudanca = 0

    #corpo cobra
    lista_cobra = []
    comprimento_cobra = 1
    
    #posiçao inicial comida
    x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0)*10.0
    y_comida = round(random.randrange(0, altura_tela - tamanho_celula) / 10.0)*10.0

    #variavel de controle do loop
    fim_jogo = False
    Perdeu = False

    while not fim_jogo:

        #verifica se player perdeu
        while perdeu:
            tela.fill(preto)
            mensagem = fonte.render("Ala perdeukjkk muito ruim. Pressione Q-Quit ou C-Continuar", True, vermelho)
            tela.blit(mensagem, [largura_tela / 8, altura_tela / 8])
            pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            #opçoes apos perder
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        perdeu = False
                    if evento.key == pygame.K_c:
                        jogo()

        #Eventos de movimento
        for evento in pygame.event.get():
            fim_jogo = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_mudanca = -tamanho_celula
                y_mudanca = 0
            elif evento.key == pygame.K_RIGHT:
                x_mudanca = tamanho_celula
                y_mudanca = 0
            elif evento.key == pygame.K.UP:
                y_mudanca = -tamanho_celula
                x_mudanca = 0
            elif evento.key == pygame.K.DOWN:
                y_mudanca = tamanho_celula
                x_mudanca = 0

        #atualiza posiçao cobra
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            perdeu = True
        x_cobra += x_mudanca
        y_cobra+= y_mudanca

        #preenche tela fundo
        tela.fill(preto)

        #desenha comida
        pygame.draw.rect(tela, vermelho, [x_comida, y_comida, tamanho_celula, tamanho_celula])

        #atualiza corpo da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        # Remove a cauda da cobra se ela nao tiver comido
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        #verifica se cobra colidiu em si mesma
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                perdeu = True

        #desenha cobra e pontuaçao
        cobra(tamanho_celula, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        #atualiza a tela
        pygame.display.update()

        #cobra come comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0)*10.0
            y_comida = round(random.randrange(0, largura_tela - tamanho_celula) / 10.0)*10.0
            comprimento_compra += 1

        #controla velocidade jogo
        clock.tick(velocidade)

    #sai do jogo
    pygame.quit()
    quit()

#inicia o jogo
jogo()