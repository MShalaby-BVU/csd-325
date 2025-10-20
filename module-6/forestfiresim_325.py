"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 10

TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = 'W'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.2  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.2  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0

# MS: Adding custom variables to set LAKE dimensions
LAKE_WIDTH = 20
LAKE_HEIGHT = 5

def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if (forest[(x, y)] == EMPTY) and (random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif (forest[(x, y)] == TREE) and (random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                # MS: If cell is a lake, set nextForest cell to lake as well
                elif forest[(x, y)] == LAKE:
                    nextForest[(x, y)] = LAKE
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)

def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # MS: Defining lake positioning and size
    lake_width = LAKE_WIDTH
    lake_height = LAKE_HEIGHT
    lake_x_pos = (WIDTH - lake_width) // 2
    lake_y_pos = (HEIGHT - lake_height) // 2

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # MS: If x, y falls within defined position as set above, make x, y a LAKE cell
            if lake_x_pos <= x < lake_x_pos + lake_width and lake_y_pos <= y < lake_y_pos + lake_height:
                forest[(x, y)] = LAKE
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            # MS: Printing LAKE
            elif forest[(x, y)] == LAKE:
                bext.fg('blue')
                print(LAKE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
