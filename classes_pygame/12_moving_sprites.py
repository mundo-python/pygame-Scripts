import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 1

		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		player.rect.x = mouse_pos[0]
		player.rect.y = mouse_pos[1]


pygame.init()

screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
	meteor = Meteor()
	meteor.rect.x = random.randrange(900)
	meteor.rect.y = random.randrange(600)

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	all_sprite_list.update()

	meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)

	for meteor in meteor_hit_list:
		score += 1
		print(score)
		
	screen.fill(WHITE)

	all_sprite_list.draw(screen)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()