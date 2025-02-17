from __future__ import print_function
import qwiic_joystick
import time
import sys
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import random

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

# color code
indicator_green = "#006400"
font_purple = "#FF00FF"
black = "#000000"
white = "#FFFFFF"

# slow cook recipes
slow_foods = {}
slow_beef_set = set()
slow_chicken_set = set()
slow_pork_set = set()
slow_vegetarian_set = set()

slow_beef_set.add("beef stew")
slow_beef_set.add("beef wellington")
slow_beef_set.add("Beef Bourguignon")

slow_chicken_set.add("Roast Chicken Breast")
slow_chicken_set.add("KFC Fried Chicken")
slow_chicken_set.add("Roast Whole Chicken")

slow_pork_set.add("Oven Roast Pork ribs")
slow_pork_set.add("Roast pork belly")

slow_vegetarian_set.add("Vegetarian meatball")
slow_vegetarian_set.add("Falafel")
slow_vegetarian_set.add("Pan roast cauliflower")

slow_foods["beef"] = slow_beef_set
slow_foods["chicken"] = slow_chicken_set
slow_foods["pork"] = slow_pork_set
slow_foods["vegetarian"] = slow_vegetarian_set

# fast cook recipes
fast_foods = {}
fast_beef_set = set()
fast_chicken_set = set()
fast_pork_set = set()
fast_vegetarian_set = set()

fast_beef_set.add("Beef curry")
fast_beef_set.add("Steak")

fast_chicken_set.add("Chicken Tikka")
fast_chicken_set.add("Tandoori Chicken")

fast_pork_set.add("Pan seared pork chop")

fast_vegetarian_set.add("Salad")
fast_vegetarian_set.add("Kung Bao Tofu")
fast_vegetarian_set.add("Cauliflower curry")

fast_foods["beef"] = fast_beef_set
fast_foods["chicken"] = fast_chicken_set
fast_foods["pork"] = fast_pork_set
fast_foods["vegetarian"] = fast_vegetarian_set

# initialize joystick
joy_stick = qwiic_joystick.QwiicJoystick()

if joy_stick.connected == False:
	print("The Qwiic Joystick device isn't connected to the system. Please check your connection", file=sys.stderr)
	joy_stick = None

joy_stick.begin()

random_food_selection = ""

# def is_joystick_up():
# 	return joy_stick.vertical == 1023

def is_joystick_down(joy_stick):
	if joy_stick.vertical == 0:
		return True

# def is_joystick_back():
# 	return joy_stick.horizontal == 0

def is_joystick_pressed(joy_stick):
	if joy_stick.button == 0:
		return True

def draw_indicator():
	# indicator box
	start_height = 1 / 4 * height
	end_height = 3 / 4 * height
	draw.rectangle((0, start_height, width, end_height), outline=0, fill=indicator_green)

	# indicator arrow
	draw.regular_polygon((width / 2, 20, 10), 3, rotation=0, fill=None, outline=None)
	draw.regular_polygon((width / 2, height - 20, 10), 3, rotation=180, fill=None, outline=None)

screens = ["time", "category", "food"]
screen_idx = 0
def switch_screens(screen_idx):
	screen_idx = 0 if screen_idx == len(screens) - 1 else screen_idx + 1
	return screen_idx

times = ["slow cooking", "fast cooking"]
time_idx = 0
def switch_cook_time(time_idx):
	time_idx = 0 if time_idx == len(times) - 1 else time_idx + 1
	return time_idx

categories = ["beef", "chicken", "pork", "vegetarian"]
category_idx = 0
def switch_categories(category_idx):
	category_idx = 0 if category_idx == len(categories) - 1 else category_idx + 1
	return category_idx

def draw_time_screen():
	draw_indicator()
	text = times[time_idx]
	draw.text((20, 1/4 * height + 10), text, font=font, fill=font_purple)

def draw_category_screen():
	draw_indicator()
	text = categories[category_idx]
	draw.text((20, 1/4 * height + 10), text, font=font, fill=font_purple)

def draw_food_screen(random_food_selection):
	if random_food_selection == "":
		food_map = slow_foods if time_idx == 0 else fast_foods
		food_set = food_map[categories[category_idx]]
		random_food_selection = random.sample(food_set, 1)[0]
		text = random_food_selection
	else:
		text = random_food_selection

	draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
	draw.text((20, 1/4 * height), "Your food suggestion:", font=font, fill=white)
	draw.text((20, 1/4 * height + 20), text, font=font, fill=font_purple)
	return text

if __name__ == '__main__':
	try:
		while True:
			screen = screens[screen_idx]
			if screen == "time":
				draw_time_screen()
				if is_joystick_down(joy_stick):
					time_idx = switch_cook_time(time_idx)

			elif screen == "category":
				draw_category_screen()
				if is_joystick_down(joy_stick):
					category_idx = switch_categories(category_idx)

			else:
				random_food_selection = draw_food_screen(random_food_selection)

			if is_joystick_pressed(joy_stick):
				screen_idx = switch_screens(screen_idx)
				random_food_selection = ""

			disp.image(image, rotation)
			time.sleep(0.2)
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\n Terminating")
		sys.exit(0)
