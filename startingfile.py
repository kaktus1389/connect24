import pygame
 
SIRINA_EKRANA = 800
VISINA_EKRANA = 800

class Interface(pygame.sprite.Sprite):
	def __init__(self,zetoni = None):
		super().__init__()
		self.zetoni = zetoni
		sirina = 450
		visina = 450
		self.image = pygame.Surface((sirina,visina))
		self.rect = self.image.get_rect()
		self.image.fill((75,200,0))
		self.rect.x = 175
		self.rect.y = 175
		
		


def main():
	ekran = pygame.display.set_mode(
		[SIRINA_EKRANA,VISINA_EKRANA])
	group = pygame.sprite.Group()
	ui = Interface()
	group.add(ui)
	ura = pygame.time.Clock()
	konec_zanke = False
	while not konec_zanke:
		ura.tick(60)
		for dogodek in pygame.event.get():
			if dogodek.type == pygame.QUIT:
				konec_zanke = True
		ekran.fill((50,50,255))
		group.draw(ekran)
		pygame.display.flip()
		
	pygame.quit()
main()
