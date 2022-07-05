from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735

screen_width = 128
screen_height = 128

serial = spi(port=0, device=1, gpio_DC=23, gpio_RST=12, gpio_LIGHT=18)
device = st7735(serial, width=screen_width, height=screen_height, persist= True, rotate=2)

rectangle_width = 10
rectangle_height = 10

pos_x = 0
pos_y = 0

canvas(device).rectangle(( pos_x , pos_y , pos_x + rectangle_width , screen_height - rectangle_height - pos_y ), outline="red", fill="red")

while True:
    direction = input('Add meg az irányt!')

    if direction == "j":
        pos_x += rectangle_width
    elif direction == "b":
        pos_x -= rectangle_width
    elif direction == "f":
        pos_y -= rectangle_height
    elif direction == "l":
        pos_y += rectangle_height

    canvas(device).clear()
    canvas(device).rectangle(( pos_x , pos_y , pos_x + rectangle_width , screen_height - rectangle_height - pos_y ), outline="red", fill="red")




