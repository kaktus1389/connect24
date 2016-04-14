import pygame
 
SIRINA_EKRANA = 1000
VISINA_EKRANA = 800
position = 0,0
s = 80
v = 80
class Interface(pygame.sprite.Sprite):
	def __init__(self,zetoni = None):
		super().__init__()
		self.zetoni = zetoni
		sirina = 800
		visina = 800
		self.image = pygame.Surface((sirina,visina))
		self.rect = self.image.get_rect()
		self.image.fill((75,200,0))
		self.rect.x = 50
		self.rect.y = 0
		
class Zeton(pygame.sprite.Sprite):
	def __init__(self,barva,x,y):
		super().__init__()
		self.image = pygame.Surface((s,v),pygame.SRCALPHA)
		pygame.draw.circle(self.image, barva, (s//2, v//2), s//2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = 0
		self.final_y = y
	def update(self):
		if self.rect.y < self.final_y:
			self.rect.y +=20
		

class VsiZetoni(object):
	def __init__(self):
		self.prvi = True
		self.zetoni = pygame.sprite.Group()
		self.polni =[0,0,0,0,0,0,0]
		self.polje = [[0 for i in range(7)] for j in range(7)]
		print(self.polje)
	def dodaj_zeton(self,pos):
		if self.prvi:
			barva = (255,40,40)
		else:
			barva = (40,255,40)
		x, y = pos
		stolpec = x // 114
		if stolpec > 6 or stolpec < 0:
			return
		x = stolpec * 114 +74
		vrstica = self.polni[stolpec]
		self.polni[stolpec]+=1
		y = 800 - vrstica*114 - 114
		if stolpec > 6 or stolpec < 0 or vrstica > 6:
			return
		self.prvi = not self.prvi
		self.zetoni.add(Zeton(barva, x, y))
		self.polje[stolpec][vrstica] = self.prvi + 1
		self.preveri_konec(vrstica, stolpec)
		print(self.polje)
	def preveri_konec(self,vrstica, stolpec):
		igralec = self.polje[stolpec][vrstica]
		v_vrsto = 1
		v_stolpec = 1
		for i in range(stolpec+1,7):
			if self.polje[i][vrstica] == igralec:
				v_vrsto += 1
			else :
				break
		for i in range(stolpec-1,-1,-1):
			if self.polje[i][vrstica] == igralec:
				v_vrsto += 1
			else :
				break
		if v_vrsto >=4:
			print("Konec")
		for i in range(vrstica+1,7):
			if self.polje[stolpec][i] == igralec:
				v_stolpec +=1
			else:
				break
		for i in range(vrstica-1,-1,-1):
			if self.polje[stolpec][i] == igralec:
				v_stolpec +=1
		if v_stolpec >=4:
			print("Konec")
	
	
	
	

	
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
		chips.zetoni.update()
						
		ekran.fill((50,50,255))
		group.draw(ekran)
		chips.zetoni.draw(ekran)
		pygame.display.flip()
		
	pygame.quit()
main()
