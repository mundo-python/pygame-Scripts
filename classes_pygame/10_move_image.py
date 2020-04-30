import pygame 

screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("background.png").convert()

player = pygame.image.load("player.png").convert()
player.set_colorkey([0, 0, 0])

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	mouse_pos = pygame.mouse.get_pos()
	x = mouse_pos[0]
	y = mouse_pos[1]

	screen.blit(background, [0, 0])
	screen.blit(player, [x, y])


	pygame.display.flip()
	clock.tick(60)

pygame.quit()