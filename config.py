import pygame
from Button import Button
import actions
import math

pygame.init()

# caps because constants
WIDTH, HEIGHT, FPS = 500, 700, 60  # display
COLUMNS, ROWS = 5, 5
MARGIN = 3
SIDE_MARGIN = 3 * MARGIN
width_without_margins = WIDTH - MARGIN * (COLUMNS - 1) - 2 * SIDE_MARGIN
SIDE_LENGTH = int(width_without_margins/COLUMNS) # convert it to int because if it is decimal it will add one pixel to one margin at some point
SIDE_MARGIN = (WIDTH - (SIDE_LENGTH * COLUMNS + MARGIN * (COLUMNS - 1))) / 2 # recalculate it to center the buttons perectly because of the int() conversion of SIDE_LENGTH
MARGIN_OPERATION = 20
WIDTH_ARROWS = 30

MAX_TEXT_WIDTH = WIDTH - 2 * (SIDE_MARGIN + WIDTH_ARROWS + MARGIN_OPERATION)

NUMBERS = '1234567890'
OPERATORS = ["+", "-", "x", "/", "^"]

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (100, 100, 100)
GREY = (80, 80, 80)
DARK_GREY = (30, 30, 30)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
DARK_BLUE = (16, 54, 97)
BLUE = (25, 85, 152)

# fonts
MAX_OPERATION_FONT_SIZE = 60
MAX_RESULT_FONT_SIZE = 80
font = [pygame.font.Font(None, i) for i in range(100)]

def merge(x1, y1, w1, h1, x2, y2, w2, h2):
    tot_width = (x2 + w2) - x1
    tot_height = (y2 + h2) - y1
    return (x1, y1, tot_width, tot_height)

std_button = (GREY, LIGHT_GREY, WHITE, font[50])
grid = [[(SIDE_MARGIN + x * (MARGIN + SIDE_LENGTH), HEIGHT - SIDE_MARGIN - SIDE_LENGTH - (ROWS - 1 - y) * (MARGIN + SIDE_LENGTH), SIDE_LENGTH, SIDE_LENGTH) for x in range(COLUMNS)] for y in range(ROWS)]

canc = Button("Canc", DARK_RED, RED, WHITE, font[40], actions.canc)
DEL = Button("DEL", DARK_GREY, GREY, WHITE, font[40], actions.delete)
left_bracket = Button("(", DARK_GREY, GREY, WHITE, font[40], actions.left)
right_bracket = Button(")", DARK_GREY, GREY, WHITE, font[40], actions.right)
other = Button("2nd", DARK_GREY, GREY, WHITE, font[40], actions.other)

decimal_point = Button(".", *std_button, actions.decimal_point)
zero = Button("0", *std_button, actions.number, n=0)
one = Button("1", *std_button, actions.number, n=1)
two = Button("2", *std_button, actions.number, n=2)
three = Button("3", *std_button, actions.number, n=3)
four = Button("4", *std_button, actions.number, n=4)
five = Button("5", *std_button, actions.number, n=5)
six = Button("6", *std_button, actions.number, n=6)
seven = Button("7", *std_button, actions.number, n=7)
eight = Button("8", *std_button, actions.number, n=8)
nine = Button("9", *std_button, actions.number, n=9)

ans = Button("Ans", DARK_BLUE, BLUE, WHITE, font[40], actions.ans)
power = Button("^", DARK_BLUE, BLUE, WHITE, font[40], actions.power, sign="^")
plus = Button("+", DARK_BLUE, BLUE, WHITE, font[40], actions.operator, sign="+")
times = Button("x", DARK_BLUE, BLUE, WHITE, font[40], actions.operator, sign="x")
equals = Button("=", DARK_BLUE, BLUE, WHITE, font[40], actions.equals)
minus = Button("-", DARK_BLUE, BLUE, WHITE, font[40], actions.minus)
divided = Button("/", DARK_BLUE, BLUE, WHITE, font[40], actions.operator, sign="/")

pi, e = map(str, (math.pi, math.e))
pi_btn = Button("π", *std_button, actions.constant, n="π")
e_btn = Button("e", *std_button, actions.constant, n="e")
e_power = Button("e^", *std_button, actions.constant, n="e^")
square = Button("x^2", *std_button, actions.power, sign="^2")
cube = Button("x^3", *std_button, actions.power, sign="^3")

root = Button("√x", *std_button, actions.root, n=2)
root3 = Button("3√x", *std_button, actions.root, n=3)
rooty = Button("y√x", *std_button, actions.rooty)
factorial = Button("!", *std_button, actions.factorial)
power_10 = Button("x10^", *std_button, actions.power_10)

# functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "ln": math.log, "log": math.log, "asin": math.asin, "acos": math.acos, "atan": math.atan, "log2": math.log2, "log10": math.log10}
# functions = ["sin", "cos", "tan", "ln", "log", "asin", "acos", "atan", "log2", "log10"]
trig = ["sin", "cos", "tan", "asin", "acos", "atan"]
logs = ["ln", "logy", "log2", "log10"]
# function_buttons = []
trig_buttons = []
logs_buttons = []

for func in trig:
    trig_buttons += [Button(func, *std_button, actions.func, func = func)]
for func in logs:
    logs_buttons += [Button(func, *std_button, actions.func, func = func)]

back = Button("<", GREY, LIGHT_GREY, WHITE, font[40], actions.back)
back.x_i, back.y_i, back.width, back.height = SIDE_MARGIN, SIDE_MARGIN, WIDTH_ARROWS, HEIGHT - 5 * SIDE_LENGTH - 4 * MARGIN - 3 * SIDE_MARGIN

next = Button(">", GREY, LIGHT_GREY, WHITE, font[40], actions.next)
next.x_i, next.y_i, next.width, next.height = WIDTH - SIDE_MARGIN - WIDTH_ARROWS, SIDE_MARGIN, WIDTH_ARROWS, HEIGHT - 5 * SIDE_LENGTH - 4 * MARGIN - 3 * SIDE_MARGIN

buttons = []
first_page = [
    [canc, DEL, left_bracket, right_bracket, other],
    [seven, eight, nine, plus, minus],
    [four, five, six, times, divided],
    [one, two, three, power, equals],
    [zero, zero, decimal_point, ans, equals]
]

second_page = [
    [canc, DEL, left_bracket, right_bracket, other],
    [pi_btn, e_btn, e_power, square, cube],
    [root, root3, rooty, factorial, power_10],
    trig_buttons[:3] + logs_buttons[:2],
    trig_buttons[3:] + logs_buttons[2:]
]

for y, row in enumerate(second_page):
    for x, button in enumerate(row):
        if button not in buttons:
            button.x_i, button.y_i, button.width, button.height = grid[y][x]
            buttons.append(button)
        else:
            for r in first_page:
                for b in r:
                    if b == button:
                        break
            button.x_i, button.y_i, button.width, button.height = merge(b.x_i, b.y_i, b.width, b.height, *grid[y][x])
second_page = buttons

buttons = []
for y, row in enumerate(first_page):
    for x, button in enumerate(row):
        if button not in buttons:
            button.x_i, button.y_i, button.width, button.height = grid[y][x]
            buttons.append(button)
        else:
            for r in first_page:
                for b in r:
                    if b == button:
                        break
            button.x_i, button.y_i, button.width, button.height = merge(b.x_i, b.y_i, b.width, b.height, *grid[y][x])
first_page = buttons

solved = False

operations = [["", ""]]
operation_index = 0
