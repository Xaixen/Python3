import pygame
import os
import random

#dimensões
tela_largura = 500
tela_altura = 800

img_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
img_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
img_background = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
img_passaro = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
               pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
               pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]

pygame.init()
fonte_pontos = pygame.font.SysFont('arial', 50)

#classes do jogo
class passaro:
    #animacões da rotação
    rotaçao_maxima = 25
    velocidade_rotacao = 20 
    tempo_animacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = img_passaro[0]
class cano:
    pass

class chao:
    pass