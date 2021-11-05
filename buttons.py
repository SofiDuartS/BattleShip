# modulo buttons
import pygame as pg

pg.init()

screen=pg.display.set_mode((700,700))

buttons_font = pg.font.Font("SKCuber-Expanded.ttf", 50) #se crea la fuente de los botones
ships_font = pg.font.Font("SKCuber-Expanded.ttf", 15)	

#-----------------BOTON START INICIO------------------------
start = buttons_font.render("START", True, (255,255,255)) #se crea el texto para el boton de inicio, ("texto", suavizado_de_texto, color_rgb)
start_hover = buttons_font.render("START", True, (0, 0, 0)) #se crea el texto para cuando el cursor está encima
start_rect = pg.Rect(400, 300, start.get_width(), start.get_height()) #se crea la zona del boton para poder presionarlo

#-----------------BOTON PLAY-------------------------------
play = buttons_font.render("PLAY", True, (255,255,255))
play_hover = buttons_font.render("PLAY", True, (0,0,0))
play_rect = pg.Rect(100, 450, play.get_width(), play.get_height())

#-----------------BOTON QUIT-----------------------------------
quit = buttons_font.render("QUIT", True, (255,255,255))
quit_hover = buttons_font.render("QUIT", True, (0,0,0))
quit_rect = pg.Rect(420, 450, quit.get_width(), quit.get_height())

#-----------------BOTONES BARCOS-------------------------------

# LISTA DE NUMEROS
uno = ships_font.render("1", True, (255,255,255))
dos = ships_font.render("2", True, (255,255,255))
tres = ships_font.render("3", True, (255,255,255))
cuatro = ships_font.render("4", True, (255,255,255))
cinco = ships_font.render("5", True, (255,255,255))
seis = ships_font.render("6", True, (255,255,255))
siete = ships_font.render("7", True, (255,255,255))
ocho = ships_font.render("8", True, (255,255,255))
nueve = ships_font.render("9", True, (255,255,255))
diez = ships_font.render("10", True, (255,255,255))

numeros_str = [uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez]

# PORTAVIONES (5 CUADROS)
portaviones= pg.image.load("portaviones.png").convert()
portaviones_rect = pg.Rect(40,600, portaviones.get_width(), (portaviones.get_height()+ cinco.get_height()))

# BUQUE (4 CUADROS)
buque= pg.image.load("buque.png").convert()
buque_rect = pg.Rect(170,600, buque.get_width(), (buque.get_height() + cuatro.get_height()))

# SUBMARINO (3 CUADROS)
submarino= pg.image.load("submarino.png").convert()
submarino_rect = pg.Rect(300,600, submarino.get_width(), (submarino.get_height() + tres.get_height()))

# CRUCEO (2 CUADROS)
crucero= pg.image.load("crucero.png").convert()
crucero_rect = pg.Rect(430,600, crucero.get_width(), (crucero.get_height() + dos.get_height()))

# LANCHA (1 CUADRO)
lancha= pg.image.load("lancha.png").convert()
lancha_rect = pg.Rect(560,600, lancha.get_width(), (lancha.get_height() + uno.get_height()))


pg.quit()