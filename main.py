
from Class import *

def MainWindow():
    pygame.init()
    #Grupo de Sprites
    sprite_list = pygame.sprite.Group()
    pygame.display.set_caption("Proyecto Basico Geometria")
    #Dibujar la ventana
    screen = pygame.display.set_mode([1280,720])
    #Add sprites
    sprite_list.add(Triangulo((0,0,255),150,0,0))
    sprite_list.add(Cuadrado((0,0,255),150,250,300))
    #Ciclo que corre la ventana principal
    run = True
    while run:
        #Eventos
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                run = False
        
        #Agregarle un colo de fondo
        screen.fill((12,183,242))
        #Dibujar sprites
        sprite_list.draw(screen)
        #Actualizar la ventana
        sprite_list.update()
        
        pygame.display.update()

    pygame.quit()
    
if __name__ == '__main__':
    MainWindow()