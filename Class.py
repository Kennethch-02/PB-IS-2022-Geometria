from cmath import cos, sin
import math
import pygame

class Triangulo(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Triangulo"
        self.color = color
        self.height = ((3)**(1/2)*lado)/2
        self.weight = lado

        #Superficie
        self.image = pygame.Surface([self.weight,self.height],pygame.SRCALPHA,32)
        #Elementos 
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        #Dibuja un triangulo
        self.firt_point = (lado/2, 0)
        self.second_point = (0,self.height)
        self.third_point = (self.weight,self.height)
        self.position = [self.firt_point,self.second_point,self.third_point]

        pygame.draw.polygon(self.image,self.color,self.position, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

class Pentagono(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Pentagono"
        self.color = color
        self.x = math.cos((72*math.pi)/180)*lado
        self.x1 = math.sin((72*math.pi)/180)*lado
        self.height = math.sin((54* math.pi)/180)*lado
        self.weight = 2*(math.cos((72*math.pi)/180)*lado) + lado
        
        #Superficie
        self.image = pygame.Surface([self.weight,self.weight],pygame.SRCALPHA,32)
        #Elementos 
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        #Dibuja un pentagono
        self.first_point = (self.weight/2, 0)
        self.second_point = (0,self.height)
        self.third_point = (self.x,self.height+self.x1)
        self.four_point = (self.x + lado,self.height+self.x1)
        self.five_point = (self.weight,self.height)

        self.position = [self.first_point,self.second_point,self.third_point,self.four_point,self.five_point]
        pygame.draw.polygon(self.image,self.color,self.position, 0)
        self.mask = pygame.mask.from_surface(self.image)
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy
class Hexagono(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Hexagono"
        self.color = color
        self.x = math.sin((60*math.pi)/180)*lado
        self.x1 = math.cos((60*math.pi)/180)*lado
        self.height = self.x*2
        self.weight = 2*self.x1 + lado
        
        #Superficie
        self.image = pygame.Surface([self.weight,self.height],pygame.SRCALPHA,32)
        #Elementos 
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        #Dibuja un hexagono
        self.first_point = (self.x1, 0)
        self.second_point = (0,self.x)
        self.third_point = (self.x1,self.height)
        self.four_point = (self.x1+lado,self.height)
        self.five_point = (self.weight,self.x)
        self.six_point = (self.x1+lado,0)

        self.position = [self.first_point,self.second_point,self.third_point,self.four_point,self.five_point,self.six_point]
        print(self.position)
        print(self.weight)
        pygame.draw.polygon(self.image,self.color,self.position, 0)
        self.mask = pygame.mask.from_surface(self.image)
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy
class Cuadrado(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Cuadrado"
        self.color = color
        self.height = lado
        self.weight = lado
        #Superficie
        self.image = pygame.Surface([self.weight, self.height], pygame.SRCALPHA, 32 )
        #Recta
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        #Dibujamos
        pygame.draw.rect(self.image,self.color,pygame.Rect(0,0,self.weight,self.height))
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy
class Circulo(pygame.sprite.Sprite):
    def __init__(self, color, radio, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Circulo"
        self.color = color
        self.weight = 2*radio
        self.height = 2*radio
        #Superficie
        self.image = pygame.Surface([self.weight, self.height], pygame.SRCALPHA, 32 )
        #Recta
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        #Dibujamos
        pygame.draw.circle(self.image,self.color,(radio,radio),radio,0)
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        self.left,self.top = pygame.mouse.get_pos()
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()
