import pygame
import botao
import random

#criar janela
altura = 900
largura = 1080
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()
janela = pygame.display.set_mode((largura, altura))
# Carrega a imagem de fundo e desenha na tela
fundo = pygame.image.load("Assets/Fundo.png")
janela.blit(fundo, (0, 0))


#Variavel caminho botoes
vermelho = pygame.image.load('Assets\Vermelho.png').convert_alpha()
verde = pygame.image.load('Assets\Verde.png').convert_alpha()
ciano = pygame.image.load('Assets\Ciano.png').convert_alpha()
cinza = pygame.image.load('Assets\Cinza.png').convert_alpha()
laranja = pygame.image.load('Assets\Laranja.png').convert_alpha()
rosa = pygame.image.load('Assets\Rosa.png').convert_alpha()
roxo = pygame.image.load('Assets\Roxo.png').convert_alpha()
amarelo = pygame.image.load('Assets\Amarelo.png').convert_alpha()
azul = pygame.image.load('Assets\Azul.png').convert_alpha()
branco = pygame.image.load('Assets\Branco.png').convert_alpha()
preto = pygame.image.load('Assets\Preto.png').convert_alpha()
sim = pygame.image.load('Assets\Sim.jpg').convert_alpha()
nao = pygame.image.load('Assets/Nao.jpg').convert_alpha()

def posiamgem():
    posy = 0
    posx = 0
    #poscao imagem no eixo Y  
    if vidas == 5:
        posy = 630
    elif vidas == 4:
        posy = 530
    elif vidas == 3:
        posy = 430
    elif vidas == 2:
        posy = 330
    elif vidas == 1:
        posy = 230
    #posicao imagem no eixo X
    if apertados == 0:
        posx = 150
    elif apertados == 1:
        posx = 360
    elif apertados == 2:
        posx = 560
    elif apertados == 3:
        posx = 760
    return posx, posy
#Criar Botões
botaoVermelho = botao.Button(50, 750, vermelho, 0.8)
botaoVerde = botao.Button(150, 750, verde, 0.8)
botaoCiano = botao.Button(250, 750, ciano, 0.8)
botaoCinza = botao.Button(350, 750, cinza, 0.8)
botaoLaranja = botao.Button(450, 750, laranja, 0.8)
botaoRosa = botao.Button(550, 750, rosa, 0.8)
botaoRoxo = botao.Button(650, 750, roxo, 0.8)
botaoAmarelo = botao.Button(750, 750, amarelo, 0.8)
botaoAzul = botao.Button(850, 750, azul, 0.8)
botaoSim = botao.Button(300 ,altura/2, sim, 0.8)
botaoNao = botao.Button(500, altura/2, nao, 0.8)
#variaveis globais
listCores = ['vermelho', 'azul', 'verde',  'laranja', 'cinza', 'ciano', 'rosa', 'roxo', 'amarelo']
senha = random.sample(listCores, 4)
senhaVazia = []
vidas = 5
apertados = 0
#gameloop
run = True
while run:
        #chamar funcao que posiciona os botoes
        posx, posy = posiamgem()
        for event in pygame.event.get():
         #sair do jogo
            if event.type == pygame.QUIT:
                       run = False
            #desenhar botoes e adicionar a variavel senhavazia
            if botaoVermelho.draw(janela):
                            print('vermelho')
                            senhaVazia.append('vermelho')
                            janela.blit(vermelho, (posx, posy))
                            apertados += 1
            elif botaoVerde.draw(janela):
                            print('verde')
                            senhaVazia.append('verde')
                            janela.blit(verde, (posx, posy))
                            apertados += 1
            elif botaoCiano.draw(janela):
                            print('ciano')
                            senhaVazia.append('ciano')
                            janela.blit(ciano, (posx, posy))
                            apertados += 1
            elif botaoCinza.draw(janela):
                            print('cinza')
                            senhaVazia.append('cinza')
                            janela.blit(cinza, (posx, posy))
                            apertados += 1
            elif botaoLaranja.draw(janela):
                            print('laranja')
                            senhaVazia.append('laranja')
                            janela.blit(laranja, (posx, posy))
                            apertados += 1
            elif botaoRosa.draw(janela):
                            print('rosa')
                            senhaVazia.append('rosa')
                            janela.blit(rosa, (posx, posy))
                            apertados += 1
            elif botaoRoxo.draw(janela):
                            print('roxo')
                            senhaVazia.append('roxo')
                            janela.blit(roxo, (posx, posy))
                            apertados += 1
            elif botaoAmarelo.draw(janela):
                            print('amarelo')
                            senhaVazia.append('amarelo')
                            janela.blit(amarelo, (posx, posy))
                            apertados += 1	
            elif botaoAzul.draw(janela):
                            print('azul')
                            senhaVazia.append('azul')
                            janela.blit(azul, (posx, posy))
                            apertados += 1
            print('SENHA:', senha)
            print("senhavazia:",senhaVazia)		
            if len(senhaVazia) == 4:
                    #compara a posicao da cor colOcada pelo usuario com a posicao da senha
                    for i in range(4):
                            #se ambas as posicoes estiverem corretas = branco
                            if senhaVazia[i] == senha[i]:
                                print("teste")
                                if i == 0:
                                        posx = 150
                                elif i == 1:
                                        posx = 360
                                elif i == 2:
                                        posx = 560
                                elif i == 3:
                                        posx = 760
                                janela.blit(branco, (posx, posy))
                            #se a cor estiver na senha porem em posicao errada preto
                            if senhaVazia[i] in senha and senhaVazia[i] != senha[i]:
                                    if i == 0:
                                        posx = 150
                                    elif i == 1:
                                        posx = 360
                                    elif i == 2:
                                        posx = 560
                                    elif i == 3:
                                        posx = 760
                                    janela.blit(preto, (posx, posy))
                    #sair do jogo quando vida acabar ou acertar senha
                    if senha == senhaVazia:
                        print('vitoria')
                        run = False
                    else:
                        vidas -= 1
                        print(vidas)
                        if vidas == 0:
                            run = False
                    apertados = 0
                    senhaVazia = []	         
        pygame.display.update()
        clock.tick(30)


