import pygame
import random

from pygame import event
from funcoes import tempo, registralog

pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
tela = pygame.display.set_mode(configTela)
fps = pygame.time.Clock()
black =(0,0,0)
white =(255,255,255)
pygame.display.set_caption("Spider-Man Game")
icone = pygame.image.load("assets/aranhaicone.png")
pygame.display.set_icon(icone)
spider = pygame.image.load("assets/miranha.png")
larguraSpider = 120
fundo = pygame.image.load("assets/imagem_fundo.jpg")
bomba = pygame.image.load("assets/bomba.png")
explosaoSom = pygame.mixer.Sound("assets/explosao1.mp3")
bombaSom = pygame.mixer.Sound("assets/bomb.mp3")
bombaSom.set_volume(0.1)
explosaoSom.set_volume(0.2)
nome = ""
email = ""
registralog(nome, email)

def mostraspider(x, y):
    tela.blit(spider, (x, y))

def mostraBomba(x, y):
    tela.blit(bomba, (x,y))

def text_objects(texto, font):
    textSurface = font.render(texto,True, black)
    return textSurface, textSurface.get_rect()

def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    tela.blit(TextSurf, TextRect)
    pygame.display.update()
    tempo(2)
    game()

def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Desvios:"+str(contador), True, white)
    tela.blit(texto, (10,10))

def morte():
    pygame.mixer.Sound.play(explosaoSom)
    pygame.mixer.music.stop()
    escreverTela("Fim de Jogo!")


def game():
    pygame.mixer.music.load("assets/musica_fundo.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    spiderPosicaoX = largura * 0.42
    spiderPosicaoY = altura * 0.8
    movimentoX = 0
    velocidade = 6
    bombaAltura = 30
    bombaLargura = 40
    bombaVelocidade = 4
    bombaX = random.randrange(0, largura - 50)
    bombaY = -40 
    desvios = 0
    pygame.mixer.Sound.play(bombaSom)

    
    while True:
        acoes = pygame.event.get()
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade * -1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        tela.fill(white)
        tela.blit(fundo,(0,0))
        escreverPlacar(desvios)
        bombaY = bombaY + bombaVelocidade
        mostraBomba(bombaX,bombaY)
        if bombaY > altura:
            bombaY = -40
            bombaX = random.randrange(0, largura - 50)
            desvios = desvios + 1
            bombaVelocidade += 0.2
            pygame.mixer.Sound.play(bombaSom)
        spiderPosicaoX += movimentoX
        if spiderPosicaoX < 0:
            spiderPosicaoX = 0
        elif spiderPosicaoX > largura - larguraSpider:
            spiderPosicaoX = largura - larguraSpider
        if spiderPosicaoY < bombaY + bombaAltura:
            if spiderPosicaoY < bombaX and spiderPosicaoX + larguraSpider > bombaX or bombaX + bombaLargura > spiderPosicaoX and bombaX + bombaLargura < spiderPosicaoX + larguraSpider:
                morte()
        mostraspider(spiderPosicaoX,spiderPosicaoY)
        pygame.display.update()
        fps.tick(60)
game()
