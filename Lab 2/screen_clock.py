import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

button = digitalio.DigitalInOut(board.D23)
button.switch_to_input()

# my design use the duration of the song numb by Linkin Park 
numb_in_second = 188

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    if button.value:
        hour = int(strftime("%H"))
        minute = int(strftime("%M"))
        second = int(strftime("%S"))
        time_in_second = hour * 3600 + minute * 60 + second
        num_of_numb = time_in_second / numb_in_second
        draw.text((0, 0), strftime("%m/%d/%Y"), font=font, fill="#FF00FF")
        draw.text((0, 20), "The song, Numb", font=font, fill="#FF00FF")
        draw.text((0, 40), "by Linkin Park", font=font, fill="#FF00FF")
        draw.text((0, 60), "has been played", font=font, fill="#FF00FF")
        draw.text((0, 80), "{:.2f}".format(num_of_numb), font=font, fill="#FF0000")
        draw.text((60, 80), " times", font=font, fill="#FF00FF")
        draw.text((0, 100), "since midnight of today", font=font, fill="#FF00FF")
    else:
        draw.text((0, 0), "where each numb lasts", font=font, fill="#FF00FF")
        draw.text((0, 20), "3:08", font=font, fill="#FF0000")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
