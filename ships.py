import pygame as pg

pg.init()

screen = pg.display.set_mode((700, 700))

class Ship: #clase para los barcos

	def __init__ (self, x, longitud, direccion=0): #recibe como parámetros coordenada en x, coordenada en y, y la cantidad de cuadros que ocupa
		self.box=x #indice de la caja en la que comienza el barco
		self.length=longitud #cantidad de cuadros que ocupa el barco
		self.direct=direccion #dirección (nota: usar flags)

	def __str__(self):
		return "Caja = {0}\t Longitud = {1}\t Direccion= {2}".format(self.box, self.length, self.direct)

	def change_direct (self): #para cambiar la direccion del barco
		if self.direct==0: #si la direccion inicial es 0
			self.direct=1 #la direccion final es 1
		elif self.direct==1: #si la direccion inicial es 1
			self.direct=0 #la direccion final es 0
		else: #si la direccion no es 1 ni 0
			direction_error = ValueError("El atributo direct solo puede tener como valores 0 y 1. Por favor verifique el codigo")
			raise direction_error # se genera un error y termina el programa

class Box: #clase para un cuadro de la cuadrícula de juego (es un boton)

	def __init__ (self, x, y): #recibe como parámetros las coordenadas de x, y
		self.area =(48,48) #area del cuadro
		self.cxy=(x,y) #coordenadas del cuadro
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

class Board: #clase para la cuadricula

	def __init__ (self): #no recibe ningun parametro
		self.x=10 #coordenada x de inicio de la cuadricula
		self.y=10 #coordenada y de inicio de la cuadricula
		self.boxes=[] #lista con objetos de la clase Box, se agregan abajo

		for i in range(100,600,50): #ciclo que itera para x
			for j in range(50,550,50): #ciclo que itera para y
				box=Box(i,j) #se crea un cuadro
				self.boxes.append(box) #se agrega a la lista
pg.display.flip()

pg.quit()
