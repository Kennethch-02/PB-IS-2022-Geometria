#Clases necesarias para la ejecucion
from Class import *

#Ventana Principal
def MainWindow():
    pygame.init()
    #Reloj
    clock = pygame.time.Clock()

    #Grupo de Sprites
    sprite_list = pygame.sprite.Group()
    sprite_list_menu = pygame.sprite.Group()
    input_group = pygame.sprite.Group()

    #Texto
    text = pygame.font.SysFont(None, 25).render("Lado o Radio", True, (255,255,255))
    pygame.display.set_caption("Proyecto Basico Geometria")
    
    #Dibujar la ventana
    screen = pygame.display.set_mode([1280,720])

    #Crear un menu
    sprite_list_menu.add(Triangulo((0,0,25),100,50,600))
    sprite_list_menu.add(Cuadrado((0,0,25),100,200,600))
    sprite_list_menu.add(Pentagono((0,0,25),60,350,600))
    sprite_list_menu.add(Hexagono((0,0,25),65,500,600))
    sprite_list_menu.add(Circulo((0,0,25),55,670,600))
    text_input = TextInputBox(125,520,100,pygame.font.SysFont(None, 25))
    input_group.add(text_input)

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
        events_list = pygame.event.get()
        for eventos in events_list:
            if eventos.type == pygame.QUIT:
                run = False
            # Cuando un boton del mause se preiona
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    mouseI = True
                elif pygame.mouse.get_pressed()[1] == True:
                    pass
                elif pygame.mouse.get_pressed()[2] == True:
                    mouseD = True
            # Cuando un boton del mause se levanta
            if eventos.type == pygame.MOUSEBUTTONUP:
                for sprites in sprite_list:
                    if(sprite_colide!=sprites and sprite_colide!=NULL):
                        if(sprites.rect.colliderect(sprite_colide.rect)):
                            sprites.inscrito = sprite_colide.type
                            sprite_colide.kill()
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
            if (Mouse.colliderect(sprites.rect)):
                sprites.color = (5,222,5)
            else:
                sprites.color = (0,0,25)
            if (Mouse.colliderect(sprites.rect) and mouseI and news_sprites == 0 and
                text_input.text.isnumeric()):
                if (sprites.type  == "Triangulo"):
                    sprite_list.add(Triangulo((255,255,0),int(text_input.text),Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Cuadrado"):
                    sprite_list.add(Cuadrado((255,255,0),int(text_input.text),Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Circulo"):
                    sprite_list.add(Circulo((255,255,0),int(text_input.text),Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Pentagono"):
                    sprite_list.add(Pentagono((255,255,0),int(text_input.text),Mouse.x,Mouse.y))
                    news_sprites = 1
                if (sprites.type  == "Hexagono"):
                    sprite_list.add(Hexagono((255,255,0),int(text_input.text),Mouse.x,Mouse.y ))
                    news_sprites = 1
        # Cuadno se mueve un sprite
        if mouseI and sprite_colide != NULL:
            sprite_colide.move(Mouse.x,Mouse.y)
            
            
        #Agregarle un colo de fondo
        screen.fill((12,183,242))
        
        #Dibujar sprites
        sprite_list.draw(screen)
        input_group.draw(screen)
        screen.blit(text,(10,525,100,100))

        #Actualizar la ventana
        Mouse.update()
        sprite_list.update()
        input_group.update(events_list)

        # Solo cuando el valor para el radio o lado es correcto, permite
        # colocar figuras
        if(text_input.text.isnumeric()):
            pygame.draw.rect(screen,(255,89,87),pygame.Rect(0,575,1280,145))
            sprite_list_menu.draw(screen)
            sprite_list_menu.update()
            
        #Valor de actualizacion
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Ejecucion de la Ventana
if __name__ == '__main__':
    MainWindow()