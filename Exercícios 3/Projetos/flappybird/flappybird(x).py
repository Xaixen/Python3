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
    imgs = img_passaro
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
        self.imagem = self.imgs[0]
    
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamneto
        self.tempo += 1
        deslocamento = 1.5 + self.tempo ** 2 + self.velocidade * self.tempo

        #restringir deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.y += deslocamento

        #o ângulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rotaçao_maxima:
                self.angulo = self.rotaçao_maxima
        else:
            if self.angulo > -90:
                self.angulo -= self.velocidade_rotacao

    def desenhar(self, tela):
        #definir  qual imagem do passaro vai usar
        self.contagem_imagem += 1
        if self.contagem_imagem < self.tempo_animacao:
            self.imagem = self.imgs[0]
        elif self.contagem_imagem < self.tempo_animacao * 2:
            self.imagem = self.imgs[1]
        elif self.contagem_imagem < self.tempo_animacao * 3:
            self.imagem = self.imgs[2]
        elif self.contagem_imagem < self.tempo_animacao * 4:
            self.imagem = self.imgs[1]
        elif self.contagem_imagem < self.tempo_animacao * 4 + 1:
            self.imagem = self.imgs[0]
            self.contagem_imagem = 0
        
        #se o passaro estiver caindo não bater asa
        if self.angulo <= -80:
            self.imagem = self.imagem[1]
            self.contagem_imagem = self.tempo_animacao * 2

        #desenhar imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_cent_img = self.imagem.get_rect(topleft = (self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = pos_cent_img)
        tela.blit(imagem_rotacionada, retangulo.topleft )

    def get_mask(self):
        #colisao
        return pygame.mask.from_surface(self.imagem)
class cano:
    distancia = 200
    velocidade = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.cano_topo = pygame.transform.flip(img_cano, False, True)
        self.cano_base = img_cano 
        self.passou = False
        self.definir_altura()
    
    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_base = self.altura + self.cano_topo.get_height()
        self.pos_base = self.altura + self.distancia
    
    def mover(self):
        self.x -= self.velocidade

    def desenhar(self, tela):
        tela.blit(self.cano_topo, (self.x, self.cano_topo))
        tela.blit(self.cano_base, (self.x, self.cano_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.cano_topo)
        base_mask = pygame.mask.from_surface(self.cano_base)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.cano_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro.mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False
        
class chao:
    pass