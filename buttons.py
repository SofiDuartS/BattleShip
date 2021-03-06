# modulo buttons
import pygame as pg

pg.init()

screen=pg.display.set_mode((700,700))

buttons_font = pg.font.Font("SKCuber-Expanded.ttf", 50) #se crea la fuente de los botones
ships_font = pg.font.Font("SKCuber-Expanded.ttf", 15) #fuente para cantidad de casillas de cada barco
boards_font = pg.font.Font("SKCuber-Expanded.ttf", 30) #fuente para indicadores de tablero en pantalla de juego

#-----------------BOTON START INICIO------------------------
start = buttons_font.render("START", True, (255,255,255)) #se crea el texto para el boton de inicio, ("texto", suavizado_de_texto, color_rgb)
start_hover = buttons_font.render("START", True, (0, 0, 255)) #se crea el texto para cuando el cursor está encima
start_rect = pg.Rect(400, 300, start.get_width(), start.get_height()) #se crea la zona del boton para poder presionarlo

#-----------------BOTON QUIT-----------------------------------
quit = buttons_font.render("QUIT", True, (255,255,255))
quit_hover = buttons_font.render("QUIT", True, (0,0,255))
quit_rect = pg.Rect(260, 450, quit.get_width(), quit.get_height())

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

# DICCIONARIO PARA LOS BOTONES
dic_buttons={5:portaviones_rect, 4:buque_rect, 3:submarino_rect, 2:crucero_rect, 1:lancha_rect}

# TEXTO PARA PANTALLA DE JUEGO
jugador1 = boards_font.render("Jugador 1: dispare", True, (255,255,255))
jugador2 = boards_font.render("Jugador 2: dispare", True, (255,255,255))

# BOTON NEXT PARA PANTALLA DE POSICIONAMIENT0
nextb = ships_font.render("next", True, (255,255,255))
nextb_hover = ships_font.render("next", True, (255,0,0))
nextb_rect = pg.Rect(620, 500, nextb.get_width(), nextb.get_height())

nextb_inst = buttons_font.render("next", True, (255,255,255))
nextb_hover_inst = buttons_font.render("next", True, (0,0,255))
nextb_rect_inst = pg.Rect(1150, 600, nextb_inst.get_width(), nextb_inst.get_height())

pg.quit()