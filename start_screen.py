# PANTALLA DE INICIO DEL JUEGO

import pygame as pg

def start_screen ():
	pg.init() #inicializamos pg

	screen = pg.display.set_mode((700,700)) #pantalla de 700*700 px
	background = pg.image.load("background.png").convert() #se crea la imagen de fondo para la pantalla de inicio
	start_font = pg.font.Font("SKCuber-Expanded.ttf", 50) #se crea la fuente del boton en la pantalla de inicio
	texto = start_font.render("START", True, (255,255,255)) #se crea el texto para el boton de inicio, ("texto", suavizado_de_texto, color_rgb)
	texto_hover = start_font.render("START", True, (0, 0, 0)) #se crea el texto para cuando el cursor está encima
	rect_boton = pg.Rect(400, 300, texto.get_width(), texto.get_height()) #se crea la zona del boton para poder presionarlo

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT:
			break

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #si hay un click en la pantalla
			if rect_boton.collidepoint(pg.mouse.get_pos()): #si el click esta dentro del area del boton
				print("click") #solo para probar si funciona el boton

		screen.blit(background, [0, 0]) #se muestra la imagen de fondo desde las coordenadas [0,0]

		if rect_boton.collidepoint(pg.mouse.get_pos()): #si el mouse está dentro de las coordenadas de rect_boton
			screen.blit(texto_hover, [400, 300]) #se muestra el texto de color negro en las coordenadas [400,300]
		else:
			screen.blit(texto, [400, 300]) #se muestra el texto de color blanco en las coordenadas [400,300]


		pg.display.flip() #se actualiza

	pg.quit()

start_screen()