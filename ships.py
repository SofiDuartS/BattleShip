import pygame as pg

pg.init()

screen = pg.display.set_mode((700, 700))

class Box: #clase para un cuadro de la cuadrícula de juego (es un boton)

	def __init__ (self, x, y): #recibe como parámetros las coordenadas de x, y
		self.area =(48,48) #area del cuadro
		self.cxy=[x,y] #coordenadas del cuadro
		self.ship=0 #estado: con o sin barco (usar flags)
		self.shoot=0 #estado: con o sin disparo (usar flags)
		self.rect=pg.Rect(self.cxy[0], self.cxy[1], self.area[0], self.area[1]) #area de click para el boton

	def accion_click_position (self, funcion, lenght, board, i, event): #board, event, i para que no haya error de declaracion de variables en la funcion
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			if self.rect.collidepoint(pg.mouse.get_pos()):
				funcion(lenght, board.boxes.index(i), 0) #board.boxes.index(i) para acceder al indice de la caja en la que se esta dando click, 0 para direccion vertical

		if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
			if self.rect.collidepoint(pg.mouse.get_pos()):
				funcion(lenght, board.boxes.index(i), 1) #board.boxes.index(i) para acceder al indice de la caja en la que se esta dando click, 1 para direccion horizontal

	def accion_click_disparo (self, funcion, board, i, event): #board, event, i para que no haya error de declaracion de variables en la funcion
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			if self.rect.collidepoint(pg.mouse.get_pos()):
				funcion(board, board.boxes.index(i)) #board.boxes.index(i) para acceder al indice de la caja en la que se esta dando click

class Board: #clase para la cuadricula

	def __init__ (self, inicio_x, fin_x): #no recibe ningun parametro
		self.boxes=[] #lista con objetos de la clase Box, se agregan abajo

		for i in range(inicio_x ,fin_x ,50): #ciclo que itera para x
			for j in range(50,550,50): #ciclo que itera para y
				box=Box(i,j) #se crea un cuadro
				self.boxes.append(box) #se agrega a la lista

	def move_player2 (self): #funcion para desplazar el tablero del jugador 2 hacia la derecha
		for i in self.boxes: #para cada caja en la lista self.boxes
			i.cxy[0]+=700 #al sumar 700 en la coordenada x, se desplaza 700px hacia la derecha
			i.rect=pg.Rect(i.cxy[0], i.cxy[1], i.area[0], i.area[1]) #para que tambien se desplacen los rectangulos de funcionamiento del boton


pg.display.flip()

pg.quit()
