# PANTALLA DE INICIO DEL JUEGO
import pygame as pg
import buttons as bt #modulo en el que se encuentran las variables de todos los botones del juego
import ships

def start_screen (): #pantalla de inicio
	pg.init() #inicializamos pg

	screen = pg.display.set_mode((700,700)) #pantalla de 700*700 px
	background = pg.image.load("background.png").convert() #se crea la imagen de fondo para la pantalla de inicio

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #si hay un click en la pantalla
			if bt.start_rect.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton
				print("click") #solo para probar si funciona el boton

		screen.blit(background, [0, 0]) #se muestra la imagen de fondo desde las coordenadas [0,0]

		if bt.start_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas de bt.start_rect
			screen.blit(bt.start_hover, [400, 300]) #se muestra el texto de color negro en las coordenadas [400,300]
		else:
			screen.blit(bt.start, [400, 300]) #se muestra el texto de color blanco en las coordenadas [400,300]


		pg.display.flip() #se actualiza

	pg.quit()

def winner_screen (): #pantalla de fin del juego (ganador)

	pg.init()

	screen = pg.display.set_mode((700,700)) #pantalla de 700*700 px
	background = pg.image.load("winner.png").convert() #se crea la imagen de fondo para la pantalla

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #si hay un click en la pantalla
			if bt.play_rect.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton PLAY
				start_screen() #se dirige a la pagina de inicio
				break #cuando se termine de ejecutar la pantalla de inicio, se rompe el ciclo para que se termine el programa
			if bt.quit_rect.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton QUIT
				break #sale del ciclo y cierra el programa

		screen.blit(background, [0, 0]) #se muestra la imagen de fondo desde las coordenadas [0,0]

		if bt.play_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas del boton PLAY
			screen.blit(bt.play_hover, [100, 450]) #se muestra el texto de color negro en las coordenadas [100,450]
		else:
			screen.blit(bt.play, [100, 450]) #se muestra el texto de color blanco en las coordenadas [100,450]

		if bt.quit_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas del boton QUIT
			screen.blit(bt.quit_hover, [420, 450]) #se muestra el texto de color negro en las coordenadas [420,450]
		else:
			screen.blit(bt.quit, [420, 450]) #se muestra el texto de color blanco en las coordenadas [420,450]


		pg.display.flip() #se actualiza

	pg.quit()

def loser_screen (): #pantalla de fin del juego (perdedor)
	#mismo codigo que winner_screen(), pero con diferente fondo de pantalla
	pg.init()

	screen = pg.display.set_mode((700,700))
	background = pg.image.load("loser.png").convert()

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			if bt.play_rect.collidepoint(pg.mouse.get_pos()):
				start_screen()
				break
			if bt.quit_rect.collidepoint(pg.mouse.get_pos()):
				break

		screen.blit(background, [0, 0])

		if bt.play_rect.collidepoint(pg.mouse.get_pos()):
			screen.blit(bt.play_hover, [100, 450])
		else:
			screen.blit(bt.play, [100, 450])

		if bt.quit_rect.collidepoint(pg.mouse.get_pos()):
			screen.blit(bt.quit_hover, [420, 450])
		else:
			screen.blit(bt.quit, [420, 450])


		pg.display.flip()

	pg.quit()

def ship_pos_screen (): #pantalla donde se posicionan los barcos
	
	pg.init()

	screen = pg.display.set_mode((700,700))
	board = ships.Board() #cuadricula, objeto de la clase Board

	screen.fill((0,0,255))

	pg.draw.rect(screen, (0,0,0), [98,48,502,502]) #para que se vea un marco negro de 2px al rededor de la cuadricula

	for i in range(100,600,50): #ciclo que itera para x
		for j in range(50,550,50): #ciclo que itera para y
			pg.draw.rect(screen, (0,0,255), [i,j,48,48],0) #se imprime la cuadricula

	for i in range(0,10): #para imprimir los numeros del 1 al 10
		screen.blit(bt.numeros_str[i], ((i*50 + (125 - bt.numeros_str[i].get_width()/2)),20))
		'''Nota:
				se accede al elemento i de la lista numeros_str del modulo buttons
				para las coordenadas (x,y): 
					x tiene i*50 para que se desplace 50px y asi los numeros queden en diferentes casillas
					x tiene (125 - bt.numeros_str[i].get_width()/2) para que cada numero quede centrado horizontalmente con la casilla
					y=20 para que todos los numeros queden al mismo nivel'''
		screen.blit(bt.numeros_str[i], ((70 - bt.numeros_str[i].get_width()/2) ,(i*50 + ((73 - bt.numeros_str[i].get_height()/2)))))
		'''Nota:
				se accede al elemento i de la lista numeros_str del modulo buttons
				para las coordenadas (x,y): 
					x = tiene (bt.numeros_str[i].get_width()/2) para que los numeros esten centrados horizontalmente
					y tiene i*50 para que se desplace 50px y asi los numeros queden en diferentes casillas
					y tiene (73 - bt.numeros_str[i].get_height()/2) para que cada numero quede centrado verticalmente con la casilla'''

	def crear_barco(lenght, a, direccion=0): #para crear barcos, a es el indice de la caja en la que da click
		if board.boxes[a].ship == 1: #si la caja esta ocupada
			pg.draw.rect(screen, (0,255,0), [board.boxes[a].cxy[0], board.boxes[a].cxy[1], 48, 48], 0) #se dibuja un cuadro verde
			pass
		else: #si la caja no esta ocupada
			ship = ships.Ship(a, lenght, direccion) #se crea un barco
			if direccion==0: #si el barco esta posicionado verticalmente
				for k in range(lenght):
					board.boxes[a+k].ship=1 #se cambia el estado de las k cajas consecutivas verticales
					pg.draw.rect(screen, (0,255,0), [board.boxes[a+k].cxy[0], board.boxes[a+k].cxy[1], 48, 48], 0) #se dibuja un cuadro verde
			else:
				for k in range(lenght):
					board.boxes[a+(10*k)].ship=1 #se cambia el estado de las k cajas consecutivas horizontales (10*k porque los indices de las cajas estan en orden vertical, se necesita multiplicar por 10 para cambiar de fila)
					pg.draw.rect(screen, (0,255,0), [board.boxes[a+10*k].cxy[0], board.boxes[a+10*k].cxy[1], 48, 48], 0) #se dibuja un cuadro verde

			print(ship) #no es necesario, pero para verificar que la longitud y direccion del barco estan bien

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #para crear barcos verticales

			if bt.portaviones_rect.collidepoint(pg.mouse.get_pos()): #si hay click en el portaviones
				print("portaviones")
				lenght=5
			if bt.buque_rect.collidepoint(pg.mouse.get_pos()): #si hay click en el buque
				print("buque")
				lenght=4
			if bt.submarino_rect.collidepoint(pg.mouse.get_pos()): #si hay click en el submarino
				print("submarino")
				lenght=3
			if bt.crucero_rect.collidepoint(pg.mouse.get_pos()): #si hay click en el crucero
				print("crucero")
				lenght=2
			if bt.lancha_rect.collidepoint(pg.mouse.get_pos()): #si hay click en el lancha
				print("lancha")
				lenght=1

			for i in board.boxes:
				i.accion_click_position(crear_barco, lenght, board, i, event)

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 3: #para crear barcos horizontales

			for i in board.boxes:
				i.accion_click_position(crear_barco, lenght, board, i, event)

		# ----- se imprimen las imagenes de los barcos -----
		screen.blit(bt.portaviones, [40,600])
		screen.blit(bt.buque, [170,600])
		screen.blit(bt.submarino, [300,600])
		screen.blit(bt.crucero, [430,600])
		screen.blit(bt.lancha, [560,600])

		# ----- se imprimen los numeros que indican la cantidad de cuadros que cada barco representa -----
		screen.blit(bt.cinco, [90-(bt.cinco.get_width()/2),650])
		screen.blit(bt.cuatro, [220-(bt.cuatro.get_width()/2),650])
		screen.blit(bt.tres, [350-(bt.tres.get_width()/2),650])
		screen.blit(bt.dos, [480-(bt.dos.get_width()/2),650])
		screen.blit(bt.uno, [610-(bt.uno.get_width()/2),650])

		pg.display.flip()

	pg.quit()

def game_screen (): #pantalla de juego
	
	pg.init()

	screen = pg.display.set_mode((1400,700))

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		screen.fill((0,0,255))

		# ----- CUADRICULA JUGADOR-----

		pg.draw.rect(screen, (0,0,0), [98,48,502,502]) 

		for i in range(100,600,50):
			for j in range(50,550,50):
				pg.draw.rect(screen, (0,0,255), [i,j,48,48],0)

		for i in range(0,10):
			screen.blit(bt.numeros_str[i], ((i*50 + (125 - bt.numeros_str[i].get_width()/2)),20))
			screen.blit(bt.numeros_str[i], ((70 - bt.numeros_str[i].get_width()/2) ,(i*50 + ((73 - bt.numeros_str[i].get_height()/2)))))

		# ----- se imprimen las imagenes de los barcos -----
		screen.blit(bt.portaviones, [40,600])
		screen.blit(bt.buque, [170,600])
		screen.blit(bt.submarino, [300,600])
		screen.blit(bt.crucero, [430,600])
		screen.blit(bt.lancha, [560,600])

		# ----- se imprimen los numeros que indican la cantidad de cuadros que cada barco representa -----
		screen.blit(bt.cinco, [90-(bt.cinco.get_width()/2),650])
		screen.blit(bt.cuatro, [220-(bt.cuatro.get_width()/2),650])
		screen.blit(bt.tres, [350-(bt.tres.get_width()/2),650])
		screen.blit(bt.dos, [480-(bt.dos.get_width()/2),650])
		screen.blit(bt.uno, [610-(bt.uno.get_width()/2),650])

		# ----- CUADRICULA PC -----

		pg.draw.rect(screen, (0,0,0), [798,48,502,502]) 

		for i in range(800,1300,50):
			for j in range(50,550,50):
				pg.draw.rect(screen, (0,0,255), [i,j,48,48],0)

		for i in range(0,10):
			screen.blit(bt.numeros_str[i], ((i*50 + (825 - bt.numeros_str[i].get_width()/2)),20))
			screen.blit(bt.numeros_str[i], ((770 - bt.numeros_str[i].get_width()/2) ,(i*50 + ((73 - bt.numeros_str[i].get_height()/2)))))

		# ----- se imprimen las imagenes de los barcos -----
		screen.blit(bt.portaviones, [740,600])
		screen.blit(bt.buque, [870,600])
		screen.blit(bt.submarino, [1000,600])
		screen.blit(bt.crucero, [1130,600])
		screen.blit(bt.lancha, [1260,600])

		# ----- se imprimen los numeros que indican la cantidad de cuadros que cada barco representa -----
		screen.blit(bt.cinco, [790-(bt.cinco.get_width()/2),650])
		screen.blit(bt.cuatro, [920-(bt.cuatro.get_width()/2),650])
		screen.blit(bt.tres, [1050-(bt.tres.get_width()/2),650])
		screen.blit(bt.dos, [1180-(bt.dos.get_width()/2),650])
		screen.blit(bt.uno, [1310-(bt.uno.get_width()/2),650])

		pg.display.flip()

	pg.quit()

#start_screen()     #para probar la pantalla de inicio
#winner_screen()    #para probar la pantalla de ganador
#loser_screen()     #para probar la pantalla de perdedor
ship_pos_screen()  #para probar la pantalla de posicionamiento de barcos
#game_screen()		#para probar la pantalla de juego