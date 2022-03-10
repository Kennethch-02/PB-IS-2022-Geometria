# Librerias utilizadas en el codigo
from asyncio.windows_events import NULL
import math
import pygame
#Clase Triangulo del tipo Sprite
class Triangulo(pygame.sprite.Sprite):
    #Funcion constructura de la Clase
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Triangulo"
        self.inscrito = ""
        self.color = color
        self.colorIns = (123,123,13)
        self.height = ((3)**(1/2)*lado)/2
        self.weight = lado
        self.lado = lado

        #Superficie
        self.image = pygame.Surface([self.weight,self.height],pygame.SRCALPHA,32)

        #Recta
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

        #Dibuja un triangulo
        self.firt_point = (lado/2, 0)
        self.second_point = (0,self.height)
        self.third_point = (self.weight,self.height)
        self.position = [self.firt_point,self.second_point,self.third_point]
        self.mask = pygame.mask.from_surface(self.image)
    
    # Funcion que contiene los metodos para dibujar el Triangulo
    # y los distintos elementos que se pueden inscribir en el
    def update(self):
        pygame.draw.polygon(self.image,self.color,self.position, 0)
        if(self.inscrito == "Circulo"):
            pygame.draw.circle(self.image,self.colorIns,(self.weight/2,self.height-self.height/3),self.height/3,0)
        elif(self.inscrito == "Triangulo"):
            pygame.draw.polygon(self.image,self.colorIns,self.position, 0)
        elif(self.inscrito == "Cuadrado"):
            x = math.tan((60*math.pi)/180)*(self.height/2)
            pygame.draw.rect(self.image,self.colorIns,pygame.Rect(x-self.lado/2,self.height/2,self.lado/2,self.lado/2))
        elif(self.inscrito == "Pentagono"):
            x = math.tan((60*math.pi)/180)*(self.height/2)
            first_point = (self.lado/2,20)
            second_point = (x-self.lado/2,self.height/2)
            third_point = (x-self.lado/2.5,self.height)
            four_point = (self.lado-(x-self.lado/2.5),self.height)
            five_point = ((x,self.height/2))
            position = [first_point,second_point,third_point,four_point,five_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
        elif(self.inscrito == "Hexagono"):
            x = math.tan((60*math.pi)/180)*(self.height/2)
            first_point = (x-self.lado/2.4,self.height/3)
            second_point = ((x-self.lado/2)/1.5,3*self.height/4.5)
            third_point = (x-self.lado/2.4,self.height)
            four_point = (self.weight-(x-self.lado/2.4),self.height)
            five_point = (self.weight-(x-self.lado/2)/1.5,3*self.height/4.5)
            six_point = (self.weight-(x-self.lado/2.4), self.height/3)
            position = [first_point,second_point,third_point,four_point,five_point,six_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)

    #Funcion para mover el sprite
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

#Clase Pentagono del tipo Sprite
class Pentagono(pygame.sprite.Sprite):
    #Funcion constructura de la Clase
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Pentagono"
        self.inscrito = ""
        self.colorIns = (123,123,13)
        self.color = color
        self.x = math.cos((72*math.pi)/180)*lado
        self.x1 = math.sin((72*math.pi)/180)*lado
        self.height = math.sin((54* math.pi)/180)*lado
        self.weight = 2*(math.cos((72*math.pi)/180)*lado) + lado
        self.lado = lado
        #Superficie
        self.image = pygame.Surface([self.weight,self.weight+20],pygame.SRCALPHA,32)
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
        self.mask = pygame.mask.from_surface(self.image)
    
    # Funcion que contiene los metodos para dibujar el Pentagono
    # y los distintos elementos que se pueden inscribir en el
    def update(self):
        pygame.draw.polygon(self.image,self.color,self.position, 0)
        if(self.inscrito == "Circulo"):
            radio =  (self.lado/2)/math.tan((36*math.pi)/180)
            pygame.draw.circle(self.image,self.colorIns,(self.weight/2,self.weight/2+15),radio,0)
        elif(self.inscrito == "Triangulo"):
            firt_point = (self.weight/2, 0)
            second_point = (self.x,self.height+self.x1)
            third_point = (self.x + self.lado,self.height+self.x1)
            position = [firt_point,second_point,third_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)

        elif(self.inscrito == "Cuadrado"):
            pygame.draw.rect(self.image,self.colorIns,pygame.Rect(self.x,self.x1-self.x1/3,self.lado,self.lado))
        elif(self.inscrito == "Pentagono"):
            pygame.draw.polygon(self.image,self.colorIns,self.position, 0)
        elif(self.inscrito == "Hexagono"):
            first_point = (self.x+self.x/1.6, self.x)
            second_point = (0,self.height)
            third_point = (self.x-self.x/5,2*self.height)
            four_point = (self.weight-self.x+self.x/5,2*self.height)
            five_point = (self.weight,self.height)
            six_point = (self.weight-self.x-self.x/1.6,self.x)
            position = [first_point,second_point,third_point,four_point,five_point,six_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
    #Funcion para mover el sprite
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

#Clase Hexagono del tipo Sprite
class Hexagono(pygame.sprite.Sprite):
    #Funcion constructura de la Clase
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        #Elementos que le pertenecen a la clase
        self.type = "Hexagono"
        self.inscrito = ""
        self.colorIns = (123,123,13)
        self.color = color
        self.x = math.sin((60*math.pi)/180)*lado
        self.x1 = math.cos((60*math.pi)/180)*lado
        self.height = self.x*2
        self.weight = 2*self.x1 + lado
        self.lado = lado
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
        self.mask = pygame.mask.from_surface(self.image)
    
    # Funcion que contiene los metodos para dibujar el Hexagono
    # y los distintos elementos que se pueden inscribir en el
    def update(self):
        pygame.draw.polygon(self.image,self.color,self.position, 0)
        if(self.inscrito == "Circulo"):
            pygame.draw.circle(self.image,self.colorIns,(self.weight/2,self.x),self.x,0)
        elif(self.inscrito == "Triangulo"):
            firt_point = (self.x1, 0)
            second_point = (self.x1,self.height)
            third_point = (self.weight,self.x)
            position = [firt_point,second_point,third_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
        elif(self.inscrito == "Cuadrado"):
            x = (self.height/2)/math.tan((60*math.pi)/180)
            l = math.tan((60*math.pi)/180)*x
            pygame.draw.rect(self.image,self.colorIns,pygame.Rect(self.x1-x/(14/5.3),x/(12.4/9),2*l-1/3*l,self.lado))
        
        elif(self.inscrito == "Pentagono"):
            first_point = (self.x1, 0)
            second_point = (0,self.x)
            third_point = (self.x1,self.height)
            four_point = (self.weight,self.x)
            five_point = (self.x1+self.lado,0)
            position = [first_point,second_point,third_point,four_point,five_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
        elif(self.inscrito == "Hexagono"):
            first_point = self.first_point
            second_point = self.second_point
            third_point = self.third_point
            four_point = self.four_point
            five_point = self.five_point
            six_point = self.six_point
            position = [first_point,second_point,third_point,four_point,five_point,six_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
    
    #Funcion para mover el sprite
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

#Clase Cuadrado del tipo Sprite
class Cuadrado(pygame.sprite.Sprite):
    #Funcion constructura de la Clase
    def __init__(self, color, lado, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Cuadrado"
        self.inscrito = ""
        self.colorIns = (123,123,13)
        self.color = color
        self.lado = lado
        self.height = lado
        self.weight = lado
        #Superficie
        self.image = pygame.Surface([self.weight, self.height], pygame.SRCALPHA, 32 )
        #Recta
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    # Funcion que contiene los metodos para dibujar el Cuadrado
    # y los distintos elementos que se pueden inscribir en el
    def update(self):
        pygame.draw.rect(self.image,self.color,pygame.Rect(0,0,self.weight,self.height))
        if(self.inscrito == "Circulo"):
            pygame.draw.circle(self.image,self.colorIns,(self.lado/2,self.lado/2),self.lado/2,0)
        elif(self.inscrito == "Triangulo"):
            firt_point = (self.lado/2, 0)
            second_point = (0,self.lado)
            third_point = (self.lado,self.lado)
            position = [firt_point,second_point,third_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)

        elif(self.inscrito == "Cuadrado"):
            pygame.draw.rect(self.image,self.colorIns,pygame.Rect(0,0,self.lado,self.lado))
        elif(self.inscrito == "Pentagono"):
            y = (self.lado/2)/math.tan((54*math.pi)/180)
            l = math.tan((36*math.pi)/180)*(self.lado/2)
            x = (self.lado - 2*l)/2
            first_point = (self.lado/2, 0)
            second_point = (0,y)
            third_point = (x,self.lado)
            four_point = (self.lado-x,self.lado)
            five_point = (self.lado,y)
            position = [first_point,second_point,third_point,four_point,five_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)

        elif(self.inscrito == "Hexagono"):
            l =  math.tan((30*math.pi)/180)*(self.lado/2)
            x = (self.lado - 2*l)/2
            first_point = (x, 0)
            second_point = (0,self.lado/2)
            third_point = (x,self.lado)
            four_point = (self.lado-x,self.lado)
            five_point = (self.lado,self.lado/2)
            six_point = (self.lado - x,0)
            position = [first_point,second_point,third_point,four_point,five_point,six_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
    
    #Funcion para mover el sprite
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

#Clase Circulo del tipo Sprite
class Circulo(pygame.sprite.Sprite):
    #Funcion constructura de la Clase
    def __init__(self, color, radio, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.type = "Circulo"
        self.inscrito = ""
        self.colorIns = (123,123,13)
        self.color = color
        self.radio = radio
        self.weight = 2*radio
        self.height = 2*radio
        #Superficie
        self.image = pygame.Surface([self.weight, self.height], pygame.SRCALPHA, 32 )
        #Recta
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    # Funcion que contiene los metodos para dibujar el Circulo
    # y los distintos elementos que se pueden inscribir en el
    def update(self):
        pygame.draw.circle(self.image,self.color,(self.radio,self.radio),self.radio,0)
        if(self.inscrito == "Circulo"):
            pygame.draw.circle(self.image,self.colorIns,(self.radio,self.radio),self.radio,0)
        elif(self.inscrito == "Triangulo"):
            lado = 2*(math.cos((30*math.pi)/180))*self.radio
            Desp_x = self.radio-lado/2
            Desp_y = (math.cos((30*math.pi)/180))*lado
            
            firt_point = (self.radio, 0)
            second_point = (Desp_x,Desp_y)
            third_point = (Desp_x+lado,Desp_y)
            position = [firt_point,second_point,third_point]

            pygame.draw.polygon(self.image,self.colorIns,position, 0)

        elif(self.inscrito == "Cuadrado"):
            x = self.radio - (math.cos((45*math.pi)/180))*self.radio
            y = self.radio - (math.cos((45*math.pi)/180))*self.radio
            lado = (self.radio/(math.sin((45*math.pi)/180)))
            pygame.draw.rect(self.image,self.colorIns,pygame.Rect(x,y,lado,lado))
        elif(self.inscrito == "Pentagono"):
            lado = 2*math.sin((31*math.pi)/180)*self.radio
            y = self.radio - math.cos((72*math.pi)/180)*self.radio
            y1 = math.cos((31*math.pi)/180)*self.radio
            z = 2*(math.sin((72*math.pi)/180)*self.radio)
            x = (2*self.radio - z)/2
            x1 = (2*self.radio-lado)/2

            first_point = (self.radio, 0)
            second_point = (x,y)
            third_point = (x1,self.radio+y1)
            four_point = (x1 + lado,self.radio+y1)
            five_point = (x+z,y)
            position = [first_point,second_point,third_point,four_point,five_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
        elif(self.inscrito == "Hexagono"):
            lado = 2*math.cos((60*math.pi)/180)*self.radio
            Desp_y = self.radio - math.sin((60*math.pi)/180)*self.radio
            x = math.sin((60*math.pi)/180)*lado
            x1 = math.cos((60*math.pi)/180)*lado
            height = x*2
            weight = 2*x1 + lado
            first_point = (x1, Desp_y)
            second_point = (0,x + Desp_y)
            third_point = (x1,height+ Desp_y)
            four_point = (x1+lado,height+ Desp_y)
            five_point = (weight,x+ Desp_y)
            six_point = (x1+lado,Desp_y)
            position = [first_point,second_point,third_point,four_point,five_point,six_point]
            pygame.draw.polygon(self.image,self.colorIns,position, 0)
    
    #Funcion para mover el sprite
    def move(self, posx, posy):
        self.rect.centerx = posx
        self.rect.centery = posy

#Clase Cursor el tipo Rect para utilizar el mouse
class Cursor(pygame.Rect):
    # Funcion constructura de la clase
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        self.left,self.top = pygame.mouse.get_pos()
    # Actualiza la posicion del mouse
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()

# Clase utilizada para contener un inputBox y 
# permitir el ingreso de datos
class TextInputBox(pygame.sprite.Sprite):
    # Funcion constructura de la clase
    def __init__(self, x, y, w, font):
        pygame.sprite.Sprite.__init__(self)
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    # Muestra o dibuja el cuadro de texto
    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)
    
    # Actualiza el texto del cuadro de texto, y su tamano
    def update(self, event_list):
        if self.active:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
            
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        self.render_text()
