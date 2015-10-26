try:
    from sense_hat import SenseHat
except ImportError:
    SenseHat = None

try:
    sense = SenseHat()
except:
    sense = None

WIDTH = 1200
HEIGHT = 1000

colours = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'yellow': (255, 255, 0),
}

def create_pixel(x, y, colour):
    pixel = Actor(colour)
    pixel.pos = x, y
    return pixel

pixels = {(x, y): create_pixel((x+1)*110, (y+1)*110, 'black') for x in range(8) for y in range(8)}

colour_palette = [create_pixel(1100, 110*(i+1), colour) for i, colour in enumerate(colours)]

def draw():
    screen.clear()
    screen.fill((0, 146, 69))
    for pixel in pixels.values():
        pixel.draw()
    for colour in colour_palette:
        colour.draw()

selected_colour = 'red'

def on_mouse_down(pos):
    global selected_colour

    for xy, pixel in pixels.items():
        if pixel.collidepoint(pos):
            pixel.image = selected_colour
            if sense:
                colour = colours[selected_colour]
                x, y = xy
                sense.set_pixel(x, y, colour)
    for colour in colour_palette:
        if colour.collidepoint(pos):
            selected_colour = colour.image
