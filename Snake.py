import pygame, sys, time, random
from pygame.locals import *

pygame.init()
play_surface = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

#---------------------------------------COMIDA DEL SNAKE-------------------------------
def food_spawn():
	food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
	return food_pos

#-----------------------------------CUERPO DEL SNAKE-------------------------------------
def snake():
	cabezaDelSnake = [100,50]
	cuerpoDelSnake = [[100,50], [90,50], [80,50]]
	
#-----------EN QUE DIRECCION VA A IR EL SNAKE CUANDO EMPIECE EL JUEGO Y DONDE VA A APARECER LA COMIDA----------
	direccion = "RIGHT"
	change = direccion
	food_pos = food_spawn()
	score = 0

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

#-------------------------------------BOTON DE MOVILIDAD DEL SNAKE-----------------------------
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					change = "RIGHT"
				if event.key == pygame.K_d:
					change = "RIGHT"

				if event.key == pygame.K_LEFT:
					change = "LEFT"
				if event.key == pygame.K_a:
					change = "LEFT"

				if event.key == pygame.K_UP:
					change = "UP"
				if event.key == pygame.K_w:
					change = "UP"

				if event.key == pygame.K_DOWN:
					change = "DOWN"
				if event.key == pygame.K_s:
					change = "DOWN"

#---------------------CODIGO PARA QUE EL SNAKE NO VAYA EN LA DIRECCION CONTRARIA A LA QUE ESTA------------------
		if change == "RIGHT" and direccion != "LEFT":
			direccion = "RIGHT"

		if change == "LEFT" and direccion != "RIGHT":
			direccion = "LEFT"

		if change == "UP" and direccion != "DOWN":
			direccion = "UP"

		if change == "DOWN" and direccion != "UP":
			direccion = "DOWN"

#---------------------CODIGO CON LA QUE EL SNAKE SE VA A MOVER-----------------------------------
		
		if direccion == "RIGHT":
			cabezaDelSnake[0] += 10 

		if direccion == "LEFT":
			cabezaDelSnake[0] -= 10 

		if direccion == "UP":
			cabezaDelSnake[1] -= 10 

		if direccion == "DOWN":
			cabezaDelSnake[1] += 10 

#-------------------LA COLA SIGA EL MOVIMIENTO DEL SNAKE------------------------------------

		cuerpoDelSnake.insert(0, list(cabezaDelSnake))
		if cabezaDelSnake == food_pos:
			food_pos = food_spawn()
			score += 1
		else:
			cuerpoDelSnake.pop()

		play_surface.fill((0,0,0))

		for pos in cuerpoDelSnake:
			pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

		pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

#--------------------------------SI SALE DE LA VENTANA GAMEOVER------------------------------------
		if cabezaDelSnake[0] >= 500 or cabezaDelSnake[0] <=0:
			print(f"Game Over! Score: {score})")
			run = False

		if cabezaDelSnake[1] >= 500 or cabezaDelSnake[1] <=0:
			print(f"Game Over! Score: {score})")
			run = False


#------------------------SI CHOCA CON SI MISMO GAMEOVER---------------------------------------
		if cabezaDelSnake in cuerpoDelSnake[1:]:
			print(f"Game Over! Score: {score})")
			run = False
#----------------------------------------------------------------------------------------------

		pygame.display.update()
		fps.tick(10)

snake()
pygame.quit()



