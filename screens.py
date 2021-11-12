# PANTALLA DE INICIO DEL JUEGO
import pygame as pg
import buttons as bt #modulo en el que se encuentran las variables de todos los botones del juego
import ships #modulo con clases para la cuadricula (Board) y cuadros que componen la cuadricula (Box)

def start_screen(): #pantalla de inicio
	pg.init() #inicializamos pg

	screen = pg.display.set_mode((700,700)) #pantalla de 700*700 px
	background = pg.image.load("background.png").convert() #se crea la imagen de fondo para la pantalla de inicio

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #si hay un click en la pantalla
			if bt.start_rect.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton
				break #para que se cierre la pantalla de inicio

		screen.blit(background, [0, 0]) #se muestra la imagen de fondo desde las coordenadas [0,0]

		if bt.start_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas de bt.start_rect
			screen.blit(bt.start_hover, [400, 300]) #se muestra el texto de color negro en las coordenadas [400,300]
		else:
			screen.blit(bt.start, [400, 300]) #se muestra el texto de color blanco en las coordenadas [400,300]


		pg.display.flip() #se actualiza

	pg.quit()

def instructions():#pantalla con las instrucciones del juego
	pg.init()
	screen = pg.display.set_mode((1400,700))
	background = pg.image.load("instrucciones.png").convert() #la imagen tiene todas las instrucciones del juego

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			if bt.nextb_rect_inst.collidepoint(pg.mouse.get_pos()): #con el boton next se cambia cierra la funcion
				break

		screen.blit(background, [0,0]) #se muestra la imagen con las instrucciones

		if bt.nextb_rect_inst.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas de bt.start_rect
			screen.blit(bt.nextb_hover_inst, [1150, 600]) #se muestra el texto de color azul en las coordenadas [1150,600]
		else:
			screen.blit(bt.nextb_inst, [1150, 600])	#se muestra el mismo texto, pero de color blanco

		pg.display.flip()

	pg.quit()

def winner_screen(winner): #pantalla de ganador, recibe como parametro el numero del jugador que gana la partida

	pg.init()

	screen = pg.display.set_mode((700,700)) #pantalla de 700*700 px
	if winner == 1: #si gana el jugador 1
		background = pg.image.load("winner1.png").convert() #el fondo de pantalla muestra que gana jugador 1
	else: #si gana el jugador 2
		background = pg.image.load("winner2.png").convert() #el fondo de pantalla muestra que gana jugador 1

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #si hay un click en la pantalla
			if bt.quit_rect.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton QUIT
				break #sale del ciclo y cierra el programa

		screen.blit(background, [0, 0]) #se muestra la imagen de fondo desde las coordenadas [0,0]


		if bt.quit_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas del boton QUIT
			screen.blit(bt.quit_hover, [260, 450]) #se muestra el texto de color negro en las coordenadas [420,450]
		else:
			screen.blit(bt.quit, [260, 450]) #se muestra el texto de color blanco en las coordenadas [420,450]


		pg.display.flip() #se actualiza

	pg.quit()

def ship_pos_screen(nombre_pantalla): #pantalla donde se posicionan los barcos, el parametro es solo para el titulo de la pantalla que se muestra
	
	pg.init()
	pg.display.set_caption(nombre_pantalla) #se cambia el titulo de la pantalla por el especificado en el parametro de la funcion

	screen = pg.display.set_mode((700,700))
	board = ships.Board(100,600) #cuadricula, objeto de la clase Board, compuesto de objetos de la clase Box
	botones = bt.dic_buttons.copy() #se crea un "clon" del diccionario del modulo buttons para que se modifique solo la copia y no el diccionario original(...)
	'''cuando no hacíamos una copia sino que declarabamos botones = bt.dic_buttons se modificaba el diccionario original, haciendo que no se pudiera ejecutar 
		ship_pos_screen() más de una vez, lo que es necesario para poder almacenar las ubicaciones de los barcos de más de un jugador'''
	screen.fill((0,0,255))

	pg.draw.rect(screen, (0,0,0), [98,48,502,502]) #para que se vea un marco negro de 2px al rededor de la cuadricula

	screen.blit(bt.nextb, [620, 500]) #para boton next de terminacion de ubicacion

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

	def crear_barco(a, lenght, direccion=0): #para crear barcos, a es el indice de la caja en la que da click
		if board.boxes[a].ship == 1: #si la caja esta ocupada
			pg.draw.rect(screen, (0,255,0), [board.boxes[a].cxy[0], board.boxes[a].cxy[1], 48, 48], 0) #se dibuja un cuadro verde
			pass
		else: #si la caja no esta ocupada
			try: # para manejo de errores
				if direccion == 0: #si el barco se quiere posicionar verticalmente
					for k in range(lenght): #se itera dentro del rango de la longitud del barco
						division = a//10
						if board.boxes[a+k].ship==1: #si alguna de las casillas en las que se debería situar el barco esta ocupada
							error_barco = ValueError("No se puede poner el barco") #se crea el error error_barco que indica que el espacio no está disponible
							raise error_barco #se "levanta" el error creado
						if (a+k)//10 != division: #si alguna de las casillas en las que se debería situar el barco está en otra fila (no hay suficiente espacio vertical para poner el barco)
							error_barco =ValueError("No se puede poner el barco") #se crea el error error_barco que indica que el espacio no está disponible
							raise error_barco #se "levanta" el error creado

				else: #si el barco se quiere posicionar horizontalmente
					for k in range(lenght): #se itera dentro del rango de la longitud del barco
						if board.boxes[a+(10*k)].ship == 1: #si alguna de las casillas en las que se debería situar el barco esta ocupada, a+(10*k) para que acceda a las casillas consecutivas hacia la derecha
							error_barco = ValueError("No se puede poner el barco") #se crea el mismo error anterior
							raise error_barco #se "levanta" el error

				#si ninguna de las dos pasa, continua con la ejecucion

				if direccion==0: #si el barco esta posicionado verticalmente
					for k in range(lenght):
						board.boxes[a+k].ship=1 #se cambia el estado de las k cajas consecutivas verticales
						pg.draw.rect(screen, (0,255,0), [board.boxes[a+k].cxy[0], board.boxes[a+k].cxy[1], 48, 48], 0) #se dibuja un cuadro verde
				else:
					for k in range(lenght):
						board.boxes[a+(10*k)].ship=1 #se cambia el estado de las k cajas consecutivas horizontales (10*k porque los indices de las cajas estan en orden vertical, se necesita multiplicar por 10 para cambiar de fila)
						pg.draw.rect(screen, (0,255,0), [board.boxes[a+10*k].cxy[0], board.boxes[a+10*k].cxy[1], 48, 48], 0) #se dibuja un cuadro verde

			except (ValueError, IndexError): #ValueError para el error que creamos, IndexError para cuando se intenta posicionar un barco de mayor longitud a las casillas disponibles en la pantalla
				print ("No se puede posicionar el barco")
				pass
		botones[lenght]=pg.Rect(0,0,0,0) #se elimina el rectangulo que le da funcionamiento al boton correspondiente para elegir la longitud del barco
		#Nota: ya no es necesario posicionar los barcos en orden ascendente de cuadros, es decir, del 1 al 5 por modificacion
		lenght=0

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #para crear barcos verticales, se da click en el boton izquierdo del mouse
			if bt.nextb_rect.collidepoint(pg.mouse.get_pos()): #cuando se da click en el rectangulo del boton next, se cierra la pantalla
				break

			try: #para manejo de errores
				if botones[5].collidepoint(pg.mouse.get_pos()): #si hay click en el portaviones
					print("portaviones")
					lenght=5
				if botones[4].collidepoint(pg.mouse.get_pos()): #si hay click en el buque
					print("buque")
					lenght=4
				if botones[3].collidepoint(pg.mouse.get_pos()): #si hay click en el submarino
					print("submarino")
					lenght=3
				if botones[2].collidepoint(pg.mouse.get_pos()): #si hay click en el crucero
					print("crucero")
					lenght=2
				if botones[1].collidepoint(pg.mouse.get_pos()): #si hay click en el lancha
					print("lancha")
					lenght=1
			except: #si ocurre algun error, no hace nada y continua con el programa
				pass

			try: #para manejo de error: cuando se intenta posicionar un barco sin haber seleccionado la longitud
				for i in board.boxes:
					i.accion_click_position(crear_barco, lenght, board, i, event)
					#para informacion sobre esta funcion, acceda a ships.py, a la clase Box

			except UnboundLocalError: #el tipo de error que se muestra en consola cuando ocurre el error
				print("Seleccione un barco para posicionar") #se le indica al jugador que seleccione una longitud
				pass

			except KeyError: #cuando se da click al area de un rectangulo de boton que ya no existe (que ya se ha usado), mostraba este error.
				pass #cuando ocurra el error, no hace nada y sigue con las instrucciones

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 3: #para crear barcos horizontales se da click derecho con el mouse

			try: #para manejo de error KeyError
				for i in board.boxes:
					i.accion_click_position(crear_barco, lenght, board, i, event)
			except KeyError: #cuando se da click al area de un rectangulo de boton que ya no existe (que ya se ha usado), mostraba este error.
				pass #cuando ocurra el error, no hace nada y sigue con las instrucciones

		if bt.nextb_rect.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas de bt.start_rect
			screen.blit(bt.nextb_hover, [620, 500]) #se muestra el texto de color negro en las coordenadas [400,300]
		else:
			screen.blit(bt.nextb, [620, 500])

		pg.display.flip()

	pg.quit()
	return board #para poder guardar los estados de los cuadros de la cuadricula, que almacenan la posicion de los barcos de un jugador, dentro de una variable en la funcion de pantalla principal de juego

def game_screen (player1, player2): #pantalla de juego
	
	score1 = 0 #almacenar el puntaje del jugador2
	attempts1 = 0 #almcenar el numero de intentos que le toma ganar al jugador 2
	score2 = 0 #almacenar el puntaje del jugador1
	attempts2 = 0 #almacenar el numero de intentos que le toma ganar al jugador 1
	turno = 1 #variable flag: cuando turno=1, solo el jugador 1 puede jugar, y cuando turno=2, solo el jugador puede jugar

	player2.move_player2() #para que se puedan mostrar los dos tableros de juego simultaneamente, mirar funcionamiento en ships.py, clase Board

	pg.init()
	pg.display.set_caption("BATTLESHIP.PY") #se cambia el titulo de la pantalla

	screen = pg.display.set_mode((1400,700))
	screen.fill((0,0,255))

	# ----- CUADRICULA JUGADOR 1-----

	pg.draw.rect(screen, (0,0,0), [98,48,502,502]) 

	for i in range(100,600,50):
		for j in range(50,550,50):
			pg.draw.rect(screen, (0,0,255), [i,j,48,48],0)

	for i in range(0,10):
		screen.blit(bt.numeros_str[i], ((i*50 + (125 - bt.numeros_str[i].get_width()/2)),20))
		screen.blit(bt.numeros_str[i], ((70 - bt.numeros_str[i].get_width()/2) ,(i*50 + ((73 - bt.numeros_str[i].get_height()/2)))))

	# ----- CUADRICULA JUGADOR 2 -----

	pg.draw.rect(screen, (0,0,0), [798,48,502,502]) 

	for i in range(800,1300,50):
		for j in range(50,550,50):
			pg.draw.rect(screen, (0,0,255), [i,j,48,48],0)

	for i in range(0,10):
		screen.blit(bt.numeros_str[i], ((i*50 + (825 - bt.numeros_str[i].get_width()/2)),20))
		screen.blit(bt.numeros_str[i], ((770 - bt.numeros_str[i].get_width()/2) ,(i*50 + ((73 - bt.numeros_str[i].get_height()/2)))))


	def disparo_player_1 (board, indice_caja): #funcion que se ejecuta cuando se da click a una casilla (cuando se dispara)
		nonlocal score1 #para poder modificar el valor del puntaje por fuera de la funcion
		nonlocal attempts1 #para poder modificar el valor de los intentos por fuera de la funcion
		nonlocal turno

		if turno == 2:
			caja_select=board.boxes[indice_caja]
			caja_select.shoot=1 #se accede al atributo shoot de la caja seleccionada y se cambia a 1 para indicar que ha sido disparada (flags)
			if caja_select.ship==1: #si la caja estaba ocupada por un barco
				pg.draw.rect(screen, (255,0,0), [caja_select.cxy[0],caja_select.cxy[1],48,48]) #se dibuja un cuadro rojo
				score1+=1 #se suma 1 punto al jugador
				attempts1+=1 #se suma 1 al total de intentos del jugador
			else: #si la caja no estaba ocupada por un barco
				pg.draw.rect(screen, (255,255,255), [caja_select.cxy[0],caja_select.cxy[1],48,48]) #se dibuja un cuadro blanco
				attempts1+=1 #se suma 1 al total de intentos del jugador
			caja_select.rect = pg.Rect(0,0,0,0) #se elimina el rectangulo que hace que el boton sea funcional para que el jugador no pueda disparar mas de una vez en cada casilla
			turno = 1

	def disparo_player_2 (board, indice_caja): #misma funcion que disparo_player_1, pero se cambian los contadores que se modifican dentro de la funcion
		nonlocal score2
		nonlocal attempts2
		nonlocal turno

		if turno == 1:
			caja_select=board.boxes[indice_caja]
			caja_select.shoot=1
			if caja_select.ship==1:
				pg.draw.rect(screen, (255,0,0), [caja_select.cxy[0],caja_select.cxy[1],48,48])
				score2+=1
				attempts2+=1
			else:
				pg.draw.rect(screen, (255,255,255), [caja_select.cxy[0],caja_select.cxy[1],48,48])
				attempts2+=1
			caja_select.rect = pg.Rect(0,0,0,0)
			turno = 2

	while True: #ciclo principal de ejecucion
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if turno == 1:
			screen.blit(bt.jugador1, (800,600))
			pg.draw.rect(screen, (0,0,255), [100,600,bt.jugador2.get_width(), bt.jugador2.get_height()])

		elif turno == 2:
			screen.blit(bt.jugador2, (100,600))
			pg.draw.rect(screen, (0,0,255), [800,600,bt.jugador1.get_width(), bt.jugador1.get_height()])

		if score1<15: #si el puntaje es menor a 15 (el jugador aun no ha ganado)
			for i in player1.boxes: #se crean los eventos que ejecutan disparo_player_1()
				i.accion_click_disparo(disparo_player_1, player1, i, event)

		elif score1==15: #si el puntaje es 15 (el jugador gana el juego)
			print("El jugador 2 ha ganado en {0} intentos".format(attempts1))
			winner = 2
			break #se rompe el ciclo

		if score2<15: #si el puntaje es menor a 15 (el jugador aun no ha ganado)
			for i in player2.boxes: #se crean los eventos que ejecutan disparo_player_1()
				i.accion_click_disparo(disparo_player_2, player2, i, event)

		elif score2==15: #si el puntaje es 15 (el jugador gana el juego)
			print("El jugador 1 ha ganado en {0} intentos".format(attempts2))
			winner = 1
			break #se rompe el ciclo

		pg.display.flip()

	pg.quit()
	return winner

#start_screen()     #para probar la pantalla de inicio
#winner_screen(2)    #para probar la pantalla de ganador
#ship_pos_screen()  #para probar la pantalla de posicionamiento de barcos
#game_screen()		#para probar la pantalla de juego
#instructions()