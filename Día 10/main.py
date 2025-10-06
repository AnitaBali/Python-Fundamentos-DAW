import pygame
import random
import math
from pygame import mixer

# Primero siempre hay que inicializar a pygame
pygame.init()

#Crear la ventana del juego o pantalla, con display y poner tupla de alto y ancho, en este caso 800-600
pantalla=pygame.display.set_mode((800,600))
se_ejecuta=True

#Título del juego
pygame.display.set_caption("Invasión Espacial") #Para dar título

#Crear variable de icono y llamarla
icono=pygame.image.load("ovni.png") #Para cargar una imagen como icono
pygame.display.set_icon(icono)

#Crear fondo
fondo=pygame.image.load("Fondo.jpg")

#Agregar música al juego
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1) #Menos 1 hace que se repita cada vez que termine

#Jugador, variables
img_jugador=pygame.image.load("astronave.png")   #64 PIXELES
#Establecer posiciones del jugador sobre el eje de x e y (horizontal, vertical)
jugador_x=368 #Dividir 800/2=400 y Dividir 64 px de la imagen entre 2, 64/2=32 RESULTADO:368
jugador_y=500 #Dividir 600-64 DE LA IMAGEN=536
jugador_x_cambio=0

#Enemigos, variables
img_enemigo=[]
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio=[]
enemigo_y_cambio=[]
cantidad_enemigos=8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("extraterrestre.png")) #64 px
    enemigo_x.append(random.randint(0,736)) #Para que el enemigo aparezca en una posición aleatoria
    enemigo_y.append(random.randint(50,200)) #Para que el enemigo aparezca en una posición aleatoria
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

#Bala, variables
img_bala=pygame.image.load("bala.png")  #64 px
bala_x=0
bala_y=500
bala_x_cambio=0
bala_y_cambio=3
bala_visible=False

#Puntos
puntaje=0
fuente=pygame.font.Font('freesansbold.ttf',32)
texto_x=10
texto_y=10

#Game Over
fuente_final=pygame.font.Font('freesansbold.ttf',40)

#Función mastrar puntos
def mostrar_puntos(x,y):
    texto=fuente.render(f"Puntos: {puntaje}", True, (255,255,255)) #Imprimir en pantalla render
    pantalla.blit(texto, (x,y))

def texto_final():
    mi_fuente_final=fuente_final.render("GAME OVER", True, (255,255,255))
    pantalla.blit(mi_fuente_final,(270,270))

#Función para dar la posición al jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))  #Arrojar al jugador en la pantalla

#Función para dar la posición al enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene], (x,y))

# Función para dar disparar bala
def disparar_bala(x, y):
    global  bala_visible
    bala_visible=True
    pantalla.blit(img_bala,(x+16,y+10))

#Función detectar colisiones
def colision(x_1,y_1,x_2,y_2):
    distancia=math.sqrt((math.pow(x_1-x_2,2))+math.pow(y_2-y_1,2))
    if distancia <27:
        return True
    else:
        return False

#Loop del juego
#Para finalizar el programa al darle a la x de salir. EL EVENTO QUIT ES PINCHAR EN SALIR, LA X ROJA
while se_ejecuta:

    #Cargar imagen de fondo
    #pantalla.fill((000, 0, 0))  # Cambiar color de fondo de la pantalla en RGB
    pantalla.blit(fondo,(0,0))

    #Iterar eventos
    for evento in pygame.event.get():

        #Evento Cerrar Juego
        if evento.type==pygame.QUIT: #EL EVENTO QUIT ES PINCHAR EN SALIR, LA X ROJA
            se_ejecuta=False

        #Evento presionar teclas
        if evento.type==pygame.KEYDOWN: #EL EVENTO KEYDOWN VERIFICA SI UNA TECLA FUE PULSADA
            ##print("una tecla fue presionada") aquí vemos si pulsa una tecla
            if evento.key==pygame.K_LEFT: #SI LA TECLA ES LA FLECHA IZQUIERDA
                jugador_x_cambio=-0.3 #establecemos pixeles a moverse
            if evento.key==pygame.K_RIGHT: #SI LA TECLA ES LA FLECHA DERECHA
                jugador_x_cambio = 0.3 #establecemos pixeles a moverse
            if evento.key==pygame.K_SPACE: #SI LA TECLA ES LA BARRA ESPACIADORA
                sonido_bala=mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x=jugador_x
                    disparar_bala(bala_x,bala_y)

        #Evento soltar flechas
        if evento.type==pygame.KEYUP: #EL EVENTO KEYDOWN VERIFICA SI UNA TECLA SE DEJO DE PULSAR
            if evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT:
                jugador_x_cambio = 0 #cuando suelte debe quedarse en el sitio

    #Modificar ubicación jugador
    jugador_x +=jugador_x_cambio

    #Mantener en los límites de la pantalla al jugador
    if jugador_x<=0:   #Para no exceder por la izquierda
        jugador_x=0
    elif jugador_x>=736:   #Para no exceder por la derecha 800-64=736
        jugador_x=736

    #Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        #Fin del juego
        if enemigo_y[e] >500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break

        enemigo_x[e] +=enemigo_x_cambio[e]

        #Mantener en los límites de la pantalla al enemigo
        if enemigo_x[e] <= 0:  # Para no exceder por la izquierda
            enemigo_x_cambio[e] = 1
            enemigo_y[e] +=enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:  # Para no exceder por la derecha 800-64=736
            enemigo_x_cambio[e] = -1
            enemigo_y[e]+= enemigo_y_cambio[e]

        # Colision
        colision_enemigo = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision_enemigo:
            sonido_colision=mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)  # Para que el enemigo aparezca en una posición aleatoria
            enemigo_y[e] = random.randint(50, 200)  # Para que el enemigo aparezca en una posición aleatoria

        enemigo(enemigo_x[e], enemigo_y[e],e)

    #Movimiento bala
    if bala_y<=-64: #Para que al llegar podamos disparar más balas, si no no dejará
        bala_y=500
        bala_visible =False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio

    jugador(jugador_x,jugador_y)

    mostrar_puntos(texto_x,texto_y)

    #Actualizar juego
    pygame.display.update()       #Hay que actualizar para que aplique el color de fondo




