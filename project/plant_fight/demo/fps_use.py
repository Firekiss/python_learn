import pygame, sys, re


pygame.init()

SIZE =  width, height = 480, 800
WHITE = pygame.Color(255, 255, 255)

img_nomal = pygame.image.load('./hero1.png')
img_run = pygame.image.load('./hero2.png')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
regex = re.compile(r'^\d*[0-4]$')

count = '-1'

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    count = int(count)
    count += 1
    count = str(count)

    # 填充背景
    screen.fill(WHITE)

    if regex.match(count):
        print(count)
        print('normal')
        screen.blit(img_nomal, (100, 100))
    else:
        print('run')
        screen.blit(img_run, (100, 100))

    
    pygame.display.flip()
