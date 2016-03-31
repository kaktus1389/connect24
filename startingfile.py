import pygame
 
SIRINA_EKRANA = 800
VISINA_EKRANA = 800
position = 0,0
s = 80
v = 80
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
		
class Zeton(pygame.sprite.Sprite):
	def __init__(self,barva,x,y):
		super().__init__()
		self.image = pygame.Surface((s,v),pygame.SRCALPHA)
		pygame.draw.circle(self.image, barva, (s//2, v//2), s//2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
class VsiZetoni(object):
	def __init__(self):
		self.prvi = True
		self.zetoni = pygame.sprite.Group()
	def dodaj_zeton(self,pos):
		if self.prvi:
			barva = (255,40,40)
		else:
			barva = (40,255,40)
		self.prvi = not self.prvi
		self.zetoni.add(Zeton(barva,pos[0],pos[1]))
class Vrstica(pygame.sprite.Sprite):
	
def main():
	ekran = pygame.display.set_mode(
		[SIRINA_EKRANA,VISINA_EKRANA])
	position = pygame.mouse.get_pos()
	group = pygame.sprite.Group()
	ui = Interface()
	group.add(ui)
	ura = pygame.time.Clock()
	konec_zanke = False
	chips = VsiZetoni()
	while not konec_zanke:
		ura.tick(60)
		for dogodek in pygame.event.get():
			if dogodek.type == pygame.QUIT:
				konec_zanke = True
			if dogodek.type == pygame.MOUSEBUTTONDOWN and len(chips.zetoni) <= 49:
				chips.dodaj_zeton(pygame.mouse.get_pos())
		
						
		ekran.fill((50,50,255))
		group.draw(ekran)
		chips.zetoni.draw(ekran)
		pygame.display.flip()
		
	pygame.quit()
main()
