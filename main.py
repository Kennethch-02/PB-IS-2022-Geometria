
from asyncio.windows_events import NULL
from msilib import type_binary
from Class import *

def MainWindow():
    pygame.init()
    #Reloj
    clock = pygame.time.Clock()
    #Grupo de Sprites
    sprite_list = pygame.sprite.Group()
    sprite_list_menu = pygame.sprite.Group()

    pygame.display.set_caption("Proyecto Basico Geometria")
    #Dibujar la ventana
    screen = pygame.display.set_mode([1280,720])
    #Crear un menu
    
    sprite_list_menu.add(Triangulo((0,0,255),100,50,600))
    sprite_list_menu.add(Cuadrado((0,0,255),100,200,600))
    sprite_list_menu.add(Pentagono((0,0,25),65,350,600))
    sprite_list_menu.add(Hexagono((0,0,25),65,500,600))
    sprite_list_menu.add(Circulo((0,0,25),55,670,600))
    #Add sprites
    Mouse = Cursor()
    sprite_colide = NULL
    news_sprites = 0
    # Boolean para cuando el boton derecho esta precionado
    mouseI = False
    mouseD = False
    #Ciclo que corre la ventana principal
    run = True
    while run:
        #Eventos
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                run = False
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    mouseI = True
                elif pygame.mouse.get_pressed()[1] == True:
                    pass
                elif pygame.mouse.get_pressed()[2] == True:
                    mouseD = True
            if eventos.type == pygame.MOUSEBUTTONUP:
                mouseI = False
                mouseD = False
                sprite_colide = NULL
                news_sprites = 0

        #Colisionns de los sprites
        for sprites in sprite_list:
            if (Mouse.colliderect(sprites.rect) and 
            mouseI and sprite_colide==NULL):
                sprite_colide = sprites

            if (Mouse.colliderect(sprites.rect) and mouseD):
                sprites.kill()

        
        #Colisiones de los sprites del Menu
        for sprites in sprite_list_menu:
            if (Mouse.colliderect(sprites.rect) and mouseI and news_sprites == 0):
                if (sprites.type  == "Triangulo"):
                    sprite_list.add(Triangulo((255,255,0),50,Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Cuadrado"):
                    sprite_list.add(Cuadrado((255,255,0),50,Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Circulo"):
                    sprite_list.add(Circulo((255,255,0),50,Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Pentagono"):
                    sprite_list.add(Pentagono((255,255,0),50,Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Hexagono"):
                    sprite_list.add(Hexagono((255,255,0),50,Mouse.x,Mouse.y))
                    news_sprites = 1

        if mouseI and sprite_colide != NULL:
            sprite_colide.move(Mouse.x,Mouse.y)

        #Agregarle un colo de fondo
        screen.fill((12,183,242))
        pygame.draw.rect(screen,(255,89,87),pygame.Rect(0,575,1280,145))
        #Dibujar sprites
        sprite_list.draw(screen)
        sprite_list_menu.draw(screen)
        #Actualizar la ventana
        Mouse.update()
        sprite_list.update()
        sprite_list_menu.update()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
if __name__ == '__main__':
    MainWindow()