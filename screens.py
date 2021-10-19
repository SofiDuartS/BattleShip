# PANTALLA DE INICIO DEL JUEGO
import pygame as pg
import buttons as bt #modulo en el que se encuentran las variables de todos los botones del juego

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

start_screen() #para que se inicialice en la pagina de inicio
# winner_screen()    solo para probar la pantalla de ganador
# loser_screen()     solo para probar la pantalla de perdedor