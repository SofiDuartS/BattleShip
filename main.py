import pygame as pg
import screens

def main():

	pg.init() #inicializamos pg

	screens.start_screen() #pantalla de inicio del juego
	screens.instructions() #pantalla con las instrucciones del juego
	jugador1=screens.ship_pos_screen("JUGADOR 1: POSICIONE SUS BARCOS") #pantalla de posicionamiento de barcos para jugador 1
	jugador2=screens.ship_pos_screen("JUGADOR 2: POSICIONE SUS BARCOS") #pantalla de posicionamiento de barcos para jugador 2
	# las anteriores se guardan en variables porque son funciones fructíferas, y se usan como parámteros para game_screen()
	ganador=screens.game_screen(jugador1, jugador2) #pantalla de juego. Se almacena en una variable porque es fructífera
	screens.winner_screen(ganador) #pantalla de finalización del juego, cambia el fondo de pantalla con el resultado dependiendo del ganador del juego

	pg.quit() #se cierra el programa

main()
