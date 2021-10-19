# modulo buttons
import pygame as pg

pg.init()


buttons_font = pg.font.Font("SKCuber-Expanded.ttf", 50) #se crea la fuente de los botones

#-----------------BOTON START INICIO------------------------
start = buttons_font.render("START", True, (255,255,255)) #se crea el texto para el boton de inicio, ("texto", suavizado_de_texto, color_rgb)
start_hover = buttons_font.render("START", True, (0, 0, 0)) #se crea el texto para cuando el cursor está encima
start_rect = pg.Rect(400, 300, start.get_width(), start.get_height()) #se crea la zona del boton para poder presionarlo

#-----------------BOTON PLAY-------------------------------
play = buttons_font.render("PLAY", True, (255,255,255))
play_hover = buttons_font.render("PLAY", True, (0,0,0))
play_rect = pg.Rect(100, 450, play.get_width(), play.get_height())

#-----------------BOTON QUIT-----------------------------------
quit = buttons_font.render("QUIT", True, (255,255,255))
quit_hover = buttons_font.render("QUIT", True, (0,0,0))
quit_rect = pg.Rect(420, 450, quit.get_width(), quit.get_height())

pg.quit()