import pygame, sys, os, pickle, pygame.freetype, time
pygame.freetype.init()
#from SCRIPZ.header import Header


os.chdir('C:/users/tdthe/downloads/PIP BOY OS ROOT/Assets/')

pygame.init
screen_width, screen_height = 876, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
running = True
zfontzs = pygame.freetype.Font(f'fonts/4_$Terminal_Font_Share-TechMono.ttf', 20)

backColr = (  0,   0,   0)
#mainColr = pygame.image.load(os.path.join('./ConditionBody0/1.png'))     #(20, 200, 20)
#mainColr = pygame.transform.scale_by(mainColr, 1)
colr = (0, 200, 100)
secolr = (0, 20, 0)
maintab = 1

class rad(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.images = []         #color.convert_alpha()
        self.index = 0
        for num in range(1, 8):
            img = pygame.image.load(f'sprites/ConditionBody0/{num}.png')
            self.images.append(img)
            self.images.append(img)
            self.images.append(img)
        
        self.image = self.images[self.index]
        
        #self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
       
        self.rect = self.image.get_rect()
        

        #pygame.image.load(os.path.join('./1.png'))


    def update(self, x):

        self.index = self.index+1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
        
        self.rect.center = (5*(screen_width/12), 5*(screen_height/12))
        #self.rect.x = 5*(screen_width/12)
        #self.rect.y = 5*(screen_height/12)


def GeneralGUI():
    pygame.draw.rect(screen, colr, (20, 30, 3, 10))
    pygame.draw.rect(screen, secolr, (40, 40,200, 30))

allem = ['', '', '', '', '', '', '', '', '', '', '']
printtime = 0
def delay_print(s):
    #if len(allem) == 11:
    del allem[1]
    allem.append('')
    for c in s:
        
        allem[10] = ((allem[10]+c))
        #time.sleep(printtime)
        screen.fill(backColr)
        #print(allem)

        zfontzs.render_to(screen, (40, 40), (allem[0]), (colr))
        zfontzs.render_to(screen, (40, 70), (allem[1]), (colr))
        zfontzs.render_to(screen, (40, 100), (allem[2]), (colr))
        zfontzs.render_to(screen, (40, 130), (allem[3]), (colr))
        zfontzs.render_to(screen, (40, 160), (allem[4]), (colr))
        zfontzs.render_to(screen, (40, 190), (allem[5]), (colr))
        zfontzs.render_to(screen, (40, 220), (allem[6]), (colr))
        zfontzs.render_to(screen, (40, 250), (allem[7]), (colr))
        zfontzs.render_to(screen, (40, 280), (allem[8]), (colr))
        zfontzs.render_to(screen, (40, 310), (allem[9]), (colr))
        zfontzs.render_to(screen, (40, 340), (allem[10]), (colr))


        pygame.display.update()

class deitrix:
    
    def Bootstrap():
        

        delay_print("010110101110010010111110011101110000100111101010111010101101")
        delay_print("101000000011111011100101011110101100111010101011001101110001")
        delay_print("110011000001100010001111110101111010100100000111010011010111")
        delay_print("100000011001011101010100011000100111101011111111011101001000")
        delay_print("000010001100001111111011010010001111100001100110010011100001")
        delay_print("111010011111111000110011000011000010010010010111001011000101")
        delay_print("110011001010001100110100000110000110100010000101001000010101")
        delay_print("001111000010001000011111001110001010111110010010011110111110")
        delay_print("010110101110010010111110011101110000100111101010111010101101")
        delay_print("101000000011111011100101011110101100111010101011001101110001")
        delay_print("110011000001100010001111110101111010100100000111010011010111")
        delay_print("100000011001011101010100011000100111101011111111011101001000")
        delay_print("000010001100001111111011010010001111100001100110010011100001")
        delay_print("111010011111111000110011000011000010010010010111001011000101")
        delay_print("110011001010001100110100000110000110100010000101001000010101")
        delay_print("001111000010001000011111001110001010111110010010011110111110")
        delay_print("010110101110010010111110011101110000100111101010111010101101")
        delay_print("101000000011111011100101011110101100111010101011001101110001")
        delay_print("110011000001100010001111110101111010100100000111010011010111")
        delay_print("100000011001011101010100011000100111101011111111011101001000")
        delay_print("000010001100001111111011010010001111100001100110010011100001")
        delay_print("111010011111111000110011000011000010010010010111001011000101")
        delay_print("110011001010001100110100000110000110100010000101001000010101")
        delay_print("001111000010001000011111001110001010111110010010011110111110")


        printtime = 0.01
        
        #delay_print((random.randint(0,1) + random.randint(0,1) + random.randint(0,1) + random.randint(0,1) + random.randint(0,1) + random.randint(0,1)))
        delay_print('*************** PIP-OS(R) V7.1.0.8 ***************')
        delay_print('')
        delay_print('')
        
        delay_print('COPYRIGHT 2075 ROBCO(R)')
        
        delay_print('LOADER V1.1')
        
        delay_print('EXEC VERSION 41.10')
        
        delay_print('64K RAM SYSTEM')
    
        delay_print('38911 BYTES FREE')
        
        delay_print('NO HOLOTAPE FOUND') #change when holotape is implemented
        
        delay_print('LOAD ROM(1): DEITRIX 303')
        time.sleep(1)


        loadimg = [pygame.image.load(f"sprites/BootSequence/92.png"), pygame.image.load(f"sprites/BootSequence/94.png"), pygame.image.load(f"sprites/BootSequence/95.png"), pygame.image.load(f"sprites/BootSequence/96.png"), pygame.image.load(f"sprites/BootSequence/97.png"), pygame.image.load(f"sprites/BootSequence/98.png"), pygame.image.load(f"sprites/BootSequence/99.png"), pygame.image.load(f"sprites/BootSequence/100.png")]
        blaberstaber = 0
        initalphas = [50, 75, 100, 125, 150, 175, 200, 225, 250, 225, 50, 75, 100, 125, 150, 175, 200, 225, 250, 225, 50, 75, 100, 125, 150, 175, 200, 225]
        
        for blarbersd in range(len(loadimg)):
            for blabersd in range(1, 4):
                blaberstaber += 1
                loadedimg = loadimg[blarbersd]
                loadrect = loadedimg.get_rect()
                loadedimg.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
                loadedimg.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
                loadrect.center = (438, 350)

                initimg = pygame.image.load(f"sprites/BootSequence/93.png")
                initrect = initimg.get_rect()
                initimg.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
                colralphad = colr + ((initalphas[blaberstaber]),)
                initimg.fill(colralphad, special_flags=pygame.BLEND_RGBA_MIN)
                initrect.center = (438, 480)

                screen.fill(backColr)
                screen.blit(loadedimg, loadrect)
                screen.blit(initimg, initrect)
                pygame.display.update()
                time.sleep(.05)



#deitrix.Bootstrap()     #make nirmal when want startup




block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

rads = rad(20, 15)
#headd = Header()
all_sprites_list.add(rads)




while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backColr)

    # RENDER YOUR GAME HERE
    
    pos = pygame.mouse.get_pos()
 
    
    #colr = (0, (pos[0] % 255), 100, 255)
    #secolr = (  0,   (pos[1] % 255),   0)
    #rads.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
    




    all_sprites_list.draw(screen)
    GeneralGUI()
    all_sprites_list.update(4)
    # flip() the display to put your work on screen
    pygame.display.update()
    
    clock.tick(32)  # limits FPS to 60

pygame.quit()