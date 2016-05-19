import pygame
from math import floor
SIRINA_EKRANA = 1000
VISINA_EKRANA = 800
position = 0,0
sirinaz = 110
visinaz = 110
marginz = 3
zmaga1 = 0
zmaga2 = 0
Runda = 0
class Interface(pygame.sprite.Sprite):
    def __init__(self,zetoni = None):
        super().__init__()
        self.zetoni = zetoni
        sirina = 800
        visina = 800
        self.image = pygame.Surface((sirina, visina), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        for i in range (8):
            razmak= i*(sirinaz+marginz)-marginz/2
            pygame.draw.line(self.image, (0, 0, 0), [razmak, 0], [razmak, 800], 3)
        for i in range (8):
                    razmak= i*(sirinaz+marginz)+2
                    pygame.draw.line(self.image, (0, 0, 0), [0, razmak], [788, razmak], 3)
        self.rect.x = 0
        self.rect.y = 0
        
class Zeton(pygame.sprite.Sprite):
    def __init__(self,barva,x,y):
        super().__init__()
        self.image = pygame.Surface((sirinaz,visinaz),pygame.SRCALPHA)
        pygame.draw.circle(self.image, barva, (sirinaz//2, visinaz//2), sirinaz//2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
        self.final_y = y
    def update(self):
        if self.rect.y < self.final_y:
                        self.rect.y +=20
        elif self.rect.y > self.final_y:
                        self.rect.y = self.final_y
        

class VsiZetoni(object):
    def __init__(self):
        self.prvi = True
        self.zetoni = pygame.sprite.Group()
        self.polni =[0,0,0,0,0,0,0]
        self.polje = [[0 for i in range(7)] for j in range(7)]
        print(self.polje)
    def nova_igra(self):
        self.zetoni.empty()
        self.polni =[0,0,0,0,0,0,0]
        self.polje = [[0 for i in range(7)] for j in range(7)]
        
    def dodaj_zeton(self,pos):
        if self.prvi:
            barva = (255,40,40)
        else:
            barva = (255,255,0)
        x, y = pos
        stolpec = floor(x / 113)
        if stolpec > 6 or stolpec < 0:
            return
        x = stolpec * (sirinaz + marginz)
        vrstica = self.polni[stolpec]
        self.polni[stolpec]+=1
        y = 800 - vrstica*(visinaz+marginz) - 118
        if stolpec > 6 or stolpec < 0 or vrstica > 6:
            return
        self.prvi = not self.prvi
        self.zetoni.add(Zeton(barva, x, y))
        self.polje[stolpec][vrstica] = self.prvi + 1
        return self.preveri_konec(vrstica, stolpec)
        print(self.polje)
        if self.prvi==True:
                    Runda +=1
                else :
                    Runda +=1
                print(Runda)
    def preveri_konec(self,vrstica, stolpec):
        igralec = self.polje[stolpec][vrstica]
        v_vrsto = 1
        v_stolpec = 1
        po_diagonali = 1
        diagonala1 = 1
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
            else:
                break
        if v_stolpec >=4:
            print("Konec")
    
        x = min(7-stolpec, 7-vrstica) 
        for i in range(1, x):
            if self.polje[stolpec+i][vrstica+i] == igralec:
                po_diagonali +=1
            else:
                break
        x = min(stolpec, vrstica)
        for i in range(1, x+1):
            if self.polje[stolpec-i][vrstica-i] == igralec:
                po_diagonali +=1
            else:
                break
        if po_diagonali >=4:
            print("Konec")
            
        x = min(stolpec,6-vrstica)
        for i in range(1,x+1):
            if self.polje[stolpec-i][vrstica+i] == igralec:
                diagonala1 +=1
            else:
                break
        x = min(6-stolpec,vrstica)
        for i in range(1,x+1):
            if self.polje[stolpec+i][vrstica-i] == igralec:
                diagonala1 +=1
            else:
                break
        if diagonala1 >=4:
            print("Konec")
        if diagonala1 >= 4 or po_diagonali >= 4 or v_vrsto >= 4 or v_stolpec >= 4:
            global zmaga1,zmaga2
            if self.prvi:
                zmaga2 += 1
            else:
                zmaga1 +=1
            return True
        return False
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
    def text(besedilo,size,x,y):
        besedilo = str(besedilo)
        pygame.font.init()
        font = pygame.font.Font(None,size)
        text = font.render(besedilo, 10, (10, 10, 10))
        textpos = text.get_rect()
        textpos.x = x
        textpos.y = y
        ekran.blit(text, textpos)
    while not konec_zanke:
        ura.tick(60)
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT:
                konec_zanke = True
            if dogodek.type == pygame.MOUSEBUTTONDOWN and len(chips.zetoni) <= 49:
                if chips.dodaj_zeton(pygame.mouse.get_pos()):
                    print("nova igra")
                    chips.nova_igra()
        chips.zetoni.update()
        ekran.fill((50,50,255))
        group.draw(ekran)
        chips.zetoni.draw(ekran)
        text("Score:",36,810,100)
        text("Red : {0}".format(zmaga1),25,810,125)
        text("Yellow: {0}".format(zmaga2),25,810,150)
        text("Na vrsti je {0}".format ("Rdeči"), 25,810,180)
        

        pygame.display.flip()
        
    pygame.quit()
main()

