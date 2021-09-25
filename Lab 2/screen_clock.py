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

# song: [name, duration in second, author]
liebestraum = ["Liebesträume", "4:53", "Franz Liszt"] 
la_campanella = ["La campanella", "4:48", "Franz Liszt"]
nocturne= ["Nocturne No. 2 Op. 9", "3:50", "Frédéric Chopin"]

def display_song_info():
    hour = int(strftime("%H"))
    text = []

    if (hour > 22 or hour < 6):
        text.append("No music info can be displayed")
        text.append("because you should be sleeping!")
    else:
        text.append("Song info:")
        if (hour >= 6 and hour < 12):
            # morning
            text.append(liebestraum[0])
            text.append("Author: " + liebestraum[2])
            text.append("Duration: " + liebestraum[1])
        elif (hour >= 12 and hour < 18):
            # afternoon
            text.append(la_campanella[0])
            text.append("Author: " + la_campanella[2])
            text.append("Duration: " + la_campanella[1])
        else:
            # night
            text.append(nocturne[0])
            text.append("Author: " + nocturne[2])
            text.append("Duration: " + nocturne[1])
    return text

def display_main_screen():
    """
    time_category: morning(6-12pm), afternoon(12-6pm), night(6-10pm), sleep(10pm-6am)
    sleeping (10pm - 6am): no music
    Morning (6 - 12pm): liebestraum, Franz Liszt
    Afternoon: (12 - 6pm): Hungarian rhapsodies, Franz Liszt
    Night (6 - 10pm): Nocturne No. 2 Op. 9 Frederic Chopin
    """
    hour = int(strftime("%H"))
    text = []

    if (hour > 22 or hour < 6):
        text.append("You should be Sleeping!")
        text.append("Good Night!")
    else:
        text.append("Time for listening to")
        if (hour >= 6 and hour < 12):
            # morning
            text.append(liebestraum[0])
            text.append("by " + liebestraum[2])
            text.append("for your morning!")
        elif (hour >= 12 and hour < 18):
            # afternoon
            text.append(la_campanella[0])
            text.append("by " + la_campanella[2])
            text.append("for your afternoon!")
        else:
            # night
            text.append(nocturne[0])
            text.append("by " + nocturne[2])
            text.append("for your evening!")
    return text



while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    texts = []
    if button.value:
        texts = display_song_info()            
    else:
        texts = display_main_screen()

    for i in range(len(texts)):
        text = texts[i]
        draw.text((0, i * 20), text, font=font, fill="#FF00FF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
