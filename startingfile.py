import pygame
 
SIRINA_EKRANA = 600
VISINA_EKRANA = 800

def main():
	ekran = pygame.display.set_mode(
		[SIRINA_EKRANA,VISINA_EKRANA])
	ekran.fill((150,100,200))
	pygame.display.flip()
	
main()
