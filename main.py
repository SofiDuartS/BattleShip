import pygame as pg
import screens

def main():
#	player1 = screens.game_screen()
#	player2 = screens.game_screen()

	pg.init() #inicializamos pg
	screen = pg.display.set_mode((700,700)) #pantalla de 700*700

	if player1<player2:
		print("El jugador 1 gana!")
	elif player1>player2:
		print("El jugador 2 gana!")
	else:
		print("Empate")

	pg.quit() #se cierra el programa

main()
