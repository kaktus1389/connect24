import pygame
 
SIRINA_EKRANA = 600
VISINA_EKRANA = 800

def main():
	ekran = pygame.display.set_mode([SIRINA_EKRANA,VISINA_EKRANA])
	konec_zanke = False
    ura = pygame.time.Clock()
    while not konec_zanke:
        ploscadi.draw(ekran)
    pygame.quit()

	ekran.fill((150,100,200))
main()
