WIDTH = 1200
HEIGHT = 1000

colours = ['black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

def create_pixel(x, y, colour):
    pixel = Actor(colour)
    pixel.pos = x, y
    return pixel

pixels = {(x, y): create_pixel((x+1)*110, (y+1)*110, 'black') for x in range(8) for y in range(8)}

colour_palette = [create_pixel(1100, 110*(i+1), colour) for i, colour in enumerate(colours)]

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
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
    for colour in colour_palette:
        if colour.collidepoint(pos):
            selected_colour = colour.image
