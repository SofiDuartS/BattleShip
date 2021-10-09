import pygame as pg

def main():
	pg.init() #inicializamos pg
	screen = pg.display.set_mode((700,700)) #pantalla de 700*700

	while True:
		event = pg.event.poll()
		if event.type == pg.QUIT: #para romper el ciclo
			break
		screen.fill((255,0,0)) #pantalla de color rojo
		pg.display.flip() #actualiza

	pg.quit() #se cierra el programa

main()
