import pygame
from pygame import mixer
import random
import math

#metodo de inicialización de pygame y acceso a todas sus herramientas
pygame.init()

#-----------------------------------------Variables--------------------------------------------------

#.display.set_mode((x,y)) establece el tamaño en que se mostrara la pantalla
ventana = pygame.display.set_mode((800,600)) #Los contenidos dentro de set_mode son el alto y ancho
#La forma correcta de ingresar el alto y ancho es en tupla

#vairable que almacenara el icono nuevo
icono = pygame.image.load("extraterrestre.png")
#Variable para el jugador
mc = pygame.image.load("cohete.png")
#Variable para la imagen de fondo
fondo = pygame.image.load("Fondo.jpg")
#Variables para la imagen de los enemigos
enemi = []
#Variable para la imagen de la bala
bala = pygame.image.load("bala.png")

#Carga de la música de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.5) #Establecimiento del volumen maximo de la musica
mixer.music.play(-1) #Ciclar música cada que termine


#Variables para la posicion del personaje jugable
jugador_x = 368
jugador_y = 500
#Variables para almacenar el movimiento en los ejes
jugador_x_cambio = 0

#Variables para la posicion de los enemigos
enemi_x = []
enemi_y = []
#Variables para almacenar el movimiento en los ejes
enemi_x_cambio = []
enemi_y_cambio = []
cantidad_enemigos = 6

#Loop para crear multiples enemigos
for e in range(cantidad_enemigos):
    #Los datos se ingresan a las listas lo que permite tener multiple enemigos de una sola vez
    enemi.append(pygame.image.load("enemigo.png"))
    enemi_x.append(random.randint(0, 736))
    enemi_y.append(random.randint(60, 100))
    enemi_x_cambio.append(0.2)
    enemi_y_cambio.append(30)

#Variables para la posicion de la bala
bala_x = 0
bala_y = 500
#Variables para almacenar el movimiento en los ejes
bala_x_cambio = 0
bala_y_cambio = 0.3
#Variable para la visisbilidad de la bala
bala_visible = False

#Variables para el puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

#Fuente del texto de Game Over
fuente_final = pygame.font.Font('freesansbold.ttf', 100)


#---------------------------------------------Metodos--------------------------------------------------

#Metodo para editar el título
pygame.display.set_caption("Marcianitos")#El contenido es el titulo a mostrar

#Metodo para modificar el icono de la ventana
pygame.display.set_icon(icono)

#--------------------------------------------Funciones-------------------------------------------------

def jugador(x, y):
    #Metodo para colocar al jugador en una posición específica
    ventana.blit(mc,(x,y))
    #.blit(imagen/modelo del pj,"tupla con cordenadas:"(x, y)

def ovnis(x, y, n):
    #Metodo para colocar los ovnis en una posición específica
    ventana.blit(enemi[n],(x,y))
    #.blit(imagen/modelo del pj,"tupla con cordenadas:"(x, y)

def disparo(x, y):
    #Volviendo la variable global podemos invertir su contenido
    global bala_visible
    bala_visible = True
    #Metodo para colocar la bala en pantalla
    ventana.blit(bala,(x + 16,y + 10))

#Funcion para calcular las distancias
def colisiones(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2,2) + math.pow(y2 - y1,2))
    if distancia < 27:
        return True
    else:
        return False

#Funcion para
def puntos(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    ventana.blit(texto, (x, y))

#Funcion mensaje de Game Over
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255,255,255))
    ventana.blit(mi_fuente_final, (85,200))

ejecucion = True #Variable para mantener la pantalla mostrada

while ejecucion:

    '''
    Metodo para cambiar el color de la pantalla
    ventana.fill((255,159,51)) Los numeros están en formato RGB
    Y de igual forma que con el alto y ancho se ingresan en un tupla
    '''
    #Metodo para insertar una imagen como fondo de la ventana
    ventana.blit(fondo, (0,0)) #("imagen", posición:(x, y))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecucion = False

        #If para corroborar las teclas presionadas
        if evento.type == pygame.KEYDOWN: #.KEYDOWN es el evento de presionar una tecla
            if evento.key == pygame.K_LEFT: #.K_LEFT hace referencia a la flecha izquierda
                jugador_x_cambio -= 0.2
            elif evento.key == pygame.K_RIGHT: #.K_RIGHT hace referencia a la flecha derecha
                jugador_x_cambio += 0.2
            elif evento.key == pygame.K_SPACE: #K_SPACE hace referencia a la barra espaciadora
                sonido_bala = mixer.Sound('disparo.mp3')
                if not bala_visible: #Verificamos si la visibilidad de la bala es falsa
                    bala_x = jugador_x
                    sonido_bala.play()
                    disparo(bala_x,bala_y)

        #If para corroborar si se suelta alguna de las flechas del teclado
        if evento.type == pygame.KEYUP: #.KEYUP es el evento de soltar una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Almacenamos el movimiento del jugador en la variable de posición en el angulo X
    jugador_x += jugador_x_cambio

    #Límites de movimiento del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #Loop para ingresar los cambios de movimiento a cada enemigo
    for e in range(cantidad_enemigos):

        #Condicion de derrota
        if enemi_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemi_y[k] = 1000
            texto_final()
            break

        # Almacenamos el movimiento de los enemigos en la variable de posición en el angulo X
        enemi_x[e] += enemi_x_cambio[e] #Siendo [e] el número de enemigos

        # Limites de movimiento de los enemigos
        if enemi_x[e] <= 0:
            enemi_x_cambio[e] = 0.2
            enemi_y[e] += enemi_y_cambio[e]
        elif enemi_x[e] >= 736:
            enemi_x_cambio[e] = -0.2
            enemi_y[e] += enemi_y_cambio[e]

        # Variable para almacenar el estado de la colision
        colison = colisiones(enemi_x[e], enemi_y[e], bala_x, bala_y)
        if colison:
            sonido_colision = mixer.Sound('Golpe.mp3')
            bala_y = 500
            bala_visible = False
            puntaje += 100
            enemi_x[e] = random.randint(0, 736)
            enemi_y[e] = random.randint(60, 100)
        # Llamada de los enemigos
        ovnis(enemi_x[e], enemi_y[e], e)

    #Verificación de la posición de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    #Movimiento de la bala
    if bala_visible:
        disparo(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Llamada del personaje jugador
    jugador(jugador_x, jugador_y)

    puntos(texto_x, texto_y)

    #Metodo para actualizar la pantalla
    pygame.display.update()
#-------------------------------------