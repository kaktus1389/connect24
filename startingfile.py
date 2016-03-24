import pygame
 
SIRINA_EKRANA = 600
VISINA_EKRANA = 800

class Interface(pygame.sprite.Sprite):
	def __init__(self,zetoni = None):
		super().__init()
		self.zetoni = zetoni
		sirina = 150
		visina = 300
		self.image = pygame.Surface((sirina,visina))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()


def main():
	ekran = pygame.display.set_mode(
		[SIRINA_EKRANA,VISINA_EKRANA])
	group = pygame.sprite.Group()
	ui = Interface()
	skupina.add(ui)
	ura = pygame.time.Clock()
	konec_zanke = False
	while not konec_zanke:
		ura.tick(60)
		for dogodek in pygame.event.get():
			if dogodek.type == pygame.QUIT:
				konec_zanke = True
		ekran.fill((200,50,50))
		pygame.display.flip()
	skupina.draw(ekran)
	pygame.quit()
main()
