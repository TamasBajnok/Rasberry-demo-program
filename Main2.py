from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735
from time import sleep
import pygame
import sys
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.setmode((128,128))
pygame.display.set_caption("keyboard_Input")
White =(255,255,255)
p1 = 10
p2 = 10
step = 5
while True:
    sur_obj.fill(White)
    pygame.draw.rect(sur_obj, (255,0,0), (p1, p2, 70, 65))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_UP]:
        p2 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K.DOWN]:
        p2 += step
    pygame.display.update()
    fpsclock.tick(fps)
#serial = spi(port=0, device=1, gpio_DC=23, gpio_RST=12, gpio_Light=18)&device = st7735(serial, width=128, height=128, persist= True, rotate=2)
# #with canvas(device) as draw:
# draw.rectangle((58,58,78,78), outline="red", fill="red")
