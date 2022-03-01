import pygame

class Triangulo(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
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

        pygame.draw.polygon(self.image,self.color,self.position, 5)
        self.mask = pygame.mask.from_surface(self.image)

class Cuadrado(pygame.sprite.Sprite):
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
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

