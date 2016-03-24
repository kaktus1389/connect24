import pygame
 
SIRINA_EKRANA = 600
VISINA_EKRANA = 800

def main():
	ekran = pygame.display.set_mode(
		[SIRINA_EKRANA,VISINA_EKRANA])
	ura = pygame.time.Clock()
	konec_zanke = False
	while not konec_zanke:
		ura.tick(60)
		for dogodek in pygame.event.get():
			if dogodek.type == pygame.QUIT:
				konec_zanke = True
		ekran.fill((150,100,200))
		pygame.display.flip()
	pygame.quit()
main()
