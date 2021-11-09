import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

screen.fill((0,0,255))

rect1 = pygame.Rect(100,100,100,100)
rect2 = pygame.Rect(100,100,100,100)
pygame.draw.rect(screen, (0,0,0), [100, 100, 100, 100])

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
		if rect1.collidepoint(pygame.mouse.get_pos()): #si hay click en el portaviones
				print("rect1")
		if rect2.collidepoint(pygame.mouse.get_pos()): #si hay click en el portaviones
				print("rect2")

	pygame.display.flip()

pygame.quit()