"""
Diccionario de funciones:
    
class:(Es parte de la programacion orientada a objetos o mejor llamada "POO")
       las clases son plantillas para definir o crear un objeto, en este caso
       las usamos para definir al jugador,el meteoro,etc.dentro de ella pueden
       haber diferentes jugadaores por ejemplo con diferentes características y
       diferentes disparos y meteoros.
       
init: Una vez que creamos un objeto o mejor dicho una clase, la tenemos que inicializar con init  
 
self: La palabra clave self se usa para acceder a todas las instancias de una clase.

función pygame sprite: sirve para las imágenes bidimensionales que utiizaremos, como la nave por ejemplo.

rect: se usa para almacenar y manipular áreas rectangulares. Un Rect puede ser creado a partir de una
     combinación de valores de izquierda, arriba, anchura y altura. También se pueden crear Rectos a partir 
     de objetos pitón que ya son Rectos o tienen un atributo llamado "rect".
     
     
image.set_colorkey: al cargar una imagen de un objeto, normalmente los bordes de esta imagen van a estar
                    en negro causando un efecto visiblemente feo por lo cual con esta funcion lo que hacemos 
                    es eliminar ese borde negro, se vera mucho en este programa.
                    
pygame.k(letra de teclado):se utiliza pra declarar justamente una letra del teclado y para saber si se aprieta
                           tal letra que haga algo en base a eso. Aca usamos las flechas para que la nave se mueva
                           
super clase: sirve para evitar tener que inicializar de vuelta una clase con cosas que ya inicializamos antes.
             En Python, puede obtener las características que desea de una superclase existente (principal) para crear una nueva subclase (secundaria). Esta característica de Python se llama herencia.

             Por herencia, puedes:

             prevalecer sobre las características de un padre o superclase.
             cambie las funciones que crea importantes.
             agregue nuevas propiedades a su hijo o subclase o clase derivada.    
             
self.kill=se eliminan todas las instancias(self) del objeto en todo  

set_volume(0.2)= mientas mas grande el numero mas alta la musica  
  
pygame.transform.scale:Cambiamos la resolucion    

sprites=sirve para que el fondo no intervenga en el movimiento del objeto o personaje
dos los objetos son instancias de algún otro, menos la clase Object que es la madre de todas. Clases
: Descripción de de objeto. Consta de una serie de métodos y datos que resumen las características de este objeto.       
"""

import pygame, random , time, bg_utils    #Importar pigeim y randoum

anchura = 1336                 #ancho de la ventana
altura = 768   
anchura2= 1400
altura2=800             #Altura de la ventana
negro = (0, 0, 0)             #Inicializamos colores
blanco = ( 255, 255, 255)
verde = (191, 255, 0)
rojo= (255, 0, 0)
pygame.init()                                        #Inicializamos pygame
pygame.mixer.init()
bg_utils.set_initial_bg(anchura2, altura2, True)                    #Inicializamos una funcion que nos ayuda con los sonidos del juego
pantalla = pygame.display.set_mode((anchura,altura),pygame.FULLSCREEN) #Creamos pantalla
pygame.display.set_caption("Space Shooter")          #Le ponemos nombre a la pantalla
reloj = pygame.time.Clock()                          #Controlar frames por segundo
keys = pygame.key.get_pressed()   
fondo= pygame.image.load("assets/star.png").convert()
fondo = pygame.transform.scale (fondo, (pantalla.get_width(), pantalla.get_height()))
x, y = 0, 0 
record = 0                          #Definimos record
record_max = 0                      #Definimos el record maximo
texto="Record: " 
pygame.mouse.set_visible(False)
                
def mostrar_texto(surface, text, size, x, y):      #definimos una funcion para mostrar texto en la pantalla con surface que nos permite elegir el lugar del texto,el texto que yo quiero mostrar, el tamaño y posiciones.
    fuente = pygame.font.SysFont("serif", size)      #Tipo de fuente de texto
    text_surface = fuente.render(text, True,blanco)  #El tipo de texto
    text_rect = text_surface.get_rect()              #Funcion rect como si fuera una imagen
    text_rect.midtop = (x, y)                        #Posicionarlo
    surface.blit(text_surface, text_rect)            #Imprimirlo  

def mostrar_vida(surface, x, y, percentage):                           #Definir vida con superficie,cordenadas y porcentaje
    barra_anchura = 150                                                #Como lo dice el nombre es la anchura de la barra de vida 
    barra_altura = 25                                                    #Esta es la altura de la barra de vida
    llenar = (percentage / 100) * barra_anchura                          #Esto es cuanto se va a llenar la barra de vida   
    borde = pygame.Rect(x, y, barra_anchura, barra_altura)               #Creamos un borde que cubre la barra
    llenar = pygame.Rect(x, y, llenar, barra_altura)                     #Vamos a llenar
    pygame.draw.rect(surface, verde, llenar)                             #Procedemos a pintar en pantalla la barra
    pygame.draw.rect(surface, blanco, borde, 2)                          #Procedemos a pintar el borde

    
def gameover():
    for counter in range(3, -1, -1):
        pantalla.blit(fondo,[0,0])
        mostrar_texto(pantalla, "Pal loby mi rey", 65, anchura // 2, altura // 3)
        mostrar_texto(pantalla, "tu record fue:",30 ,anchura // 2.2, altura // 1.9)
        mostrar_texto(pantalla,str(record),27,anchura//1.8,altura//1.9)
        mostrar_texto(pantalla, "Volverás a la pantalla en " + str(counter) + " ...", 30, anchura //2, altura//1.5)
        pygame.display.flip()
        time.sleep(1)
    
def pantalla_de_inicio():                                                             #Definimos la pantalla de inicio
    pantalla.blit(fondo, [0,0])                                                         #Colocamos el fondo de siempre
    mostrar_texto(pantalla, "Space Shooter", 65, anchura // 2, altura // 4)                       #Mostramos texto 
    mostrar_texto(pantalla, "Presione enter para jugar", 30, anchura // 2, altura // 2) #Mostramos texto,
    mostrar_texto(pantalla,"¡Desbloquea nuevas skins a medida que ganes puntos!",27,anchura//2,altura*2/3)
    mostrar_texto(pantalla,"Presione 'esc' para salir del juego",20,anchura//9,altura*6.5/7)
    mostrar_texto(pantalla,"The GAYmers Foundation",20,anchura//1.08,altura*6.5/7)
    mostrar_texto(pantalla, "Creadores:",25,anchura//1.08,altura//7/75)
    mostrar_texto(pantalla, "Bárbara Martín ",20,anchura//1.075,altura//5.5/1.05)
    mostrar_texto(pantalla, "Milagros Ricci",20,anchura//1.08,altura//6/1.8)
    mostrar_texto(pantalla, "Lara Tolosa",20,anchura//1.08,altura//5.5/4.5)
    mostrar_texto(pantalla, "Maximiliano Mora",20,anchura//1.08,altura//5/3)
    mostrar_texto(pantalla, "Julián Martini",20,anchura//1.08,altura//4.5/1.85)
    mostrar_texto(pantalla, "Leandro Mercado",20,anchura//1.08, altura//3.8/1.81)
    pygame.display.flip()                                                               #Mostramos en pantalla
    waiting = True                                                                      #Si estamos esperando
    while waiting:                                                                      #Mientras esperando
        try:
            for event in pygame.event.get():                                                #Si pasa algoel juegoscierra
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit() 
                
                if event.type == pygame.KEYDOWN:                                              #Si se toca una tecla jugamos juego
                    if event.key == pygame.K_RETURN:
                        waiting = False
        except Exception as e:
            print(str(e))
            pygame.quit()
            break
            
class Jugador(pygame.sprite.Sprite):                                    #Creamos nuestra clase jugador
    def __init__(self, all_sprites, balas, laser_sound, bala_skin):                                                 #Inicilizamos la clase
        super().__init__()                                               #Definimos la superclase
        self.image = pygame.image.load("assets/nave2.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro)                                   #con esta funcion eliminamos el fondo negro que aparece con la imagen
        self.bala_skin = bala_skin
        self.rect = self.image.get_rect()                                #Ponemos el cuadro del sprite (impagen bidimensional)
        self.rect.centerx = anchura // 2
        self.rect.bottom = altura - 10
        self.rect.centery = altura//2
        self.rect.top = anchura -10
        self.velocidad_x= 0                                              #En estas dos lineas definimos la velocidad y y la velocidad x para luego usarlas
        self.laser_sound = laser_sound
        self.balas = balas
        self.all_sprites = all_sprites
        self.velocidad_y= 0
        self.vida = 100
            
    def set_bala_skin(self, bala_skin):
        self.bala_skin = bala_skin
 
    def update(self):                              
        self.velocidad_x = 0                          #Velocidadx del bicho=0
        self.velocidad_y= 0                           #Velocidady del bicho=0
        keystate = pygame.key.get_pressed()           #Si una tecla es presionada 
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:                   #Revisar si la tecla que se pulso es la izquierda
            self.velocidad_x = -9                   #la velocidad es de -5 asi nos movemos hacia la izquierda
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:                  #Si la tecla que se pulso es la derecha
            self.velocidad_x = 9                     #la velocidad es de 5 asi nos movemos a la derecha
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:                     #Si la tecla que se pulso es la de arriba
            self.velocidad_y = -9                  #la velocidad es de -5 para que se mueva hacia arriba
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:                   #Si la tecla que se pulsó es la de abajo 
            self.velocidad_y = 9                    #la velocidad es de 5 para que se mueva abajo
        self.rect.y += self.velocidad_y               #Usamos la funcion rect y l velocidad para que la imagen pueda moverse sin problemas
        self.rect.x += self.velocidad_x               #Lo mismo que arriba    
        if self.rect.right > anchura:                 #Aca nos fijamos que el jugador no pueda moverse mas del ancho y largo de pantalla
            self.rect.right = anchura
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top< 0:
            self.rect.top=0
        if self.rect.bottom> altura:
            self.rect.bottom = altura 
            
    def disparo(self):                                  
        bala = Bala(self.rect.centerx, self.rect.top, self.bala_skin)      #Le damos una posicion a la bala desde el centro de la nave hasta el top de la ventana del juego
        self.all_sprites.add(bala)
        self.balas.add(bala)
        self.laser_sound.play()
  
    def skin(self):                                                 
        self.image = pygame.image.load("assets/srek.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro)    
                               
    def skin1(self):
        self.image = pygame.image.load("assets/c.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro) 
        
    def skin2(self):
        self.image = pygame.image.load("assets/pepa.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro)  
        
    def skin3(self):
        self.image = pygame.image.load("assets/benji.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro)
    
    def skin4(self):
        self.image = pygame.image.load("assets/benji.png").convert()    #Cargamos la imagen del jugador y lo convertimos para que no quede mal
        self.image.set_colorkey(negro)
        
        
class Meteoro(pygame.sprite.Sprite):                  #Definimos una clase llamada meteoro para programar los meteoros
    def __init__(self, meteor_images):                               #Inicializamos la clase
        super().__init__()                             #Inicializamos la super clase
        self.image = random.choice(meteor_images)      #Elegimos un meteoro al azar con random.choice
        self.image.set_colorkey(negro)                 #Usamos la funcion para eliminar borde negro
        self.rect = self.image.get_rect()                           #Obtenemos una recta
        self.rect.x = random.randrange(anchura - self.rect.width)   #Aca podemos elegir al azar donde aparecen
        self.rect.y = random.randrange(-120, -100)                  #Lo mismo de la linea de arriba
        self.velocidady = random.randrange(5, 20)                  #Velocidad aleatoria
        self.velocidadx = random.randrange(-5, 15)                   #movimiento horizontal aleatorio
        self.golpe = pygame.mixer.Sound("assets/ugh.wav")
        
    def update(self):
        self.rect.y += self.velocidady                                                            #Usamos la funcion rect y l velocidad para que la imagen pueda moverse sin problemas      
        self.rect.x += self.velocidadx                                                            #Usamos la funcion rect y l velocidad para que la imagen pueda moverse sin problemas   
        if self.rect.top > altura + 10 or self.rect.left < -40 or self.rect.right > anchura + 40: #Si el tope del meteoro rebazo el tope de la ventana 
            self.rect.x = random.randrange(anchura - self.rect.width)                             #Repetir el meteoro para que no se acaben
            self.rect.y = random.randrange(-178, - 100)
            self.velocidady = random.randrange(1, 10)

class Bala(pygame.sprite.Sprite):                                #Implementamos  elobjeto bala
    def __init__(self, x, y, image_path):                                    #lo inicializamos  
        super().__init__()                                        #Definimos una super clase 
        self.image = pygame.image.load(image_path)       #Cargamos la imagen de la bala
        self.image.set_colorkey(negro)                            #Evitamos los bordes negros
        self.rect = self.image.get_rect()                         #Usamos la funcion rect
        self.rect.y = y
        self.rect.centerx = x
        self.velocidady = -10                                     #Definimos la velocidad y negativa para que empiece desde abajo

    def update(self):                                            #Definimos el movimiento de la bala
        self.rect.y += self.velocidady                            #Usamos la funcion rect y l velocidad para que la imagen pueda moverse sin problemas 
        if self.rect.bottom < 0:                                  #Eliminamos todas las instancias del objeto de cualquier lista
            self.kill()  
 
 
class Explosion(pygame.sprite.Sprite):                           #Creamos el objeto explosion 
    def __init__(self, center, explosion_image, explosion_anim):                                  #Lo inicializamos y la centramos
        super().__init__()                                        #Creamos una superclase 
        self.image = explosion_image                           #Cargamos la imagen y la incializamos de la imagen 0
        self.rect = self.image.get_rect()                         #utilizamos la funcion rect para las imagenes bidimensionales
        self.rect.center = center                                 #Centramos la imagen 
        self.frame = 0                                            #Creamos el frame para luego dar la ilusion de animacion
        self.explosion_anim = explosion_anim
        self.last_update = pygame.time.get_ticks()                #Saber exactamente cuanto tiempo transcurrio para poder hacer la animacion           
        self.frame_rate = 50                                      # VELOCIDAD DE LA EXPLOSION

    def update(self):                                            #Definimos el movimiento
        now = pygame.time.get_ticks()                             #Esta funcion permite saber cuanto tiempo transcurrio cuando se crea la explosion
        if now - self.last_update > self.frame_rate:              #Si transcurrieron mas de 50 milisegundos vamos a inicializar la explosion 
            self.last_update = now                                
            self.frame += 1                                       #Incrementamso la variable
            if self.frame == len(self.explosion_anim):                 #averiguar si ya llegue al final de la lista
                self.kill()                                       #Entonces elimino todos los self
            else:                                                 #Si no creamos la explosion
                center = self.rect.center                         
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center      
                

meteor_images = []
meteor_list = ["assets/1.png", "assets/2.png", "assets/3.png", "assets/4.png",
                "assets/5.png", "assets/6.png", "assets/7.png" ] #Cargamos las imagenes de los diferentes tipos de meteoros en una lista
for img in meteor_list:
    meteor_images.append(pygame.image.load(img).convert()) #Convertimos la lista grande en la lista vacia


explosion_anim = []                                    #Creamos una lista vacía
for i in range(9):                                     #Creamos un bucle for
    file = "assets/regularExplosion0{}.png".format(i)  #Invocamos las imagenes de explosiones
    img = pygame.image.load(file).convert()            #Convertimos la imagen
    img.set_colorkey(negro)                            #Evitamos el borde negro
    img_scale = pygame.transform.scale(img, (70,70))   #Escalamos la imagen para que no pese tanto y mejore la calidad de vista
    explosion_anim.append(img_scale)                   #Lo guardamos en la lista vacia 

# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/es.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/spase.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1) #Reproducimos musica principal y que se repita indefinidamente


fin_juego = True
running = True

while running:                              #Bucle principal
    if fin_juego:   
        pantalla_de_inicio()                #Mostrar pantalla de inicio
        fin_juego = False
        all_sprites = pygame.sprite.Group() #creamos un grupo
        meteor_list = pygame.sprite.Group() #Creamos otro grupo para los meteoros
        balas = pygame.sprite.Group()       #Creamos un grupo para las balas
        jugador =Jugador(all_sprites, balas, laser_sound, "assets/laser1.png")                 #Creamos la instancia jugador
        all_sprites.add(jugador)            #Almacenamos el jugador en el grupo 
        for i in range(8):                  #Almacenamos los meteoros en los grupos
            meteoro = Meteoro(meteor_images)             
            all_sprites.add(meteoro)        
            meteor_list.add(meteoro)
        record = 0                          #Reseteamos el record
     
    reloj.tick(60)  #Definimos 60 frames x segundo
    for event in pygame.event.get():       
        if event.type == pygame.KEYDOWN:  #Note que presione una tecla
            if event.key == pygame.K_SPACE: #Monitorear la barra espacidora y ver si la aprieta
                jugador.disparo()             #Si la aprieta que dispare
            if event.key==pygame.K_ESCAPE:
                if event.key==pygame.K_ESCAPE:
                    from tkinter import messagebox
                    prompt = messagebox.askokcancel(title = "Confirmar",
                            message = "Desea cerrar el juego?")
                    if prompt == True:
                        running = False
        

    keys = pygame.key.get_pressed()    
    	# Control del audio
    	# Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:     #si toco la tecla 9 y el sonido esta por encima de 0
    	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)            #le bajo el volumen en un nivel
    	# Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:               #si toco la tecla 0 y el volumen es menor a 1 (el maximo)
    	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)   #le incremento volumen de a 0,01

    	# Desactivar sonido
    elif keys[pygame.K_2]:                          #si toco la tecla m
    	pygame.mixer.music.set_volume(0.0)           #el volumen se pone en 0

    	# Reactivar sonido
    elif keys[pygame.K_1]:                      #si toco la tecla ,
    	pygame.mixer.music.set_volume(1.0)          #pongo el volumen en 1 (que es el maximo)
    all_sprites.update()
    
    #Skins
    if record >= 1000:
        jugador.skin3()
        jugador.set_bala_skin("assets/bala5.png")
    elif record >= 750:
        jugador.skin2()
        jugador.set_bala_skin("assets/bala4.png")
    elif record >= 500:
        jugador.skin1()
        jugador.set_bala_skin("assets/bala3.png")
    elif record >= 250:
        jugador.skin()
        jugador.set_bala_skin("assets/bala2.png")
    
    golpes = pygame.sprite.groupcollide(meteor_list, balas, True, True)  #Los objetos de distintos grupos que colisionan van a desaparecer,se agregan dos trues para que las balas y el meteoro desaparezcan
    for golpe in golpes:
        record += 10                             #Cada vez que se golpea el meteoro y la bala se agregan 10 puntos
        if record > record_max:
            record_max = record
        explosion_sound.play()                   #Cada vez que colisionan suena el sonido de explosion
        explosion =Explosion(golpe.rect.center, explosion_anim[0] , explosion_anim) #Colocar la explosion en el punto de golpe y que este centrada
        all_sprites.add(explosion)               #Almacenamos la explosion
        meteoro = Meteoro(meteor_images)                      #Agregamos y almacenamos mas meteoros
        all_sprites.add(meteoro)
        meteor_list.add(meteoro)  
         
    # Chocar colisiones - jugador - meteoro
    golpes = pygame.sprite.spritecollide(jugador, meteor_list, True)   #Los objetos que se choquen van a desaparecer, se le agrega un true para que desaparezca el meteoro
    for golpe in golpes:
        jugador.vida -= 15
        meteoro.golpe.play()
        meteoro=Meteoro(meteor_images)                                        
        all_sprites.add(meteoro)
        meteor_list.add(meteoro)
    if jugador.vida <= 0:                                          #Si la vida es menor o igual a cero es el fin del juego
            fin_juego = True  
    if fin_juego== True:
        gameover()
        
    y_relativa = y % fondo.get_rect().height
    pantalla.blit(fondo, (x, y_relativa - fondo.get_rect().height))
    
    if y_relativa < anchura:
         pantalla.blit(fondo, (0, y_relativa))
    y += 10
    reloj.tick(60)
                                      
    all_sprites.draw(pantalla)  #mostramos todos los sprites en la pantalla
    
    #Marcador
    mostrar_texto(pantalla, str(record), 30, anchura // 2, 10)         #Mostramos el record escrito con la posicion    
    mostrar_texto(pantalla, str(record_max), 30, anchura // 1.02, 10)     #mostramos el record maximo escrito con la posicion  
    mostrar_texto(pantalla, str(texto), 30, anchura // 1.08, 10)
    # vida.
    mostrar_vida(pantalla, 5, 5, jugador.vida)                         #mostramos la vida de la nave
    pygame.display.flip()     
                                        
pygame.quit()                                                          #Cerramos pygame

