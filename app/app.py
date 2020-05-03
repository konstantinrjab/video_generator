import moviepy.editor as mpy
from random import randrange
import random

VIDEO_SIZE = (640, 480)
DURATION = 5
TREE_RANGE_HEIGHT = (220, 320)
TREE_DENSITY = 4

WHITE = (255, 255, 255)

background_path = './assets/background.png'
background = mpy.ImageClip(background_path). \
    set_position(('center', 0)). \
    resize(width=VIDEO_SIZE[0])


def get_trees(count):
    tree_paths = [
        './assets/tree1.png',
        './assets/tree2.png',
        './assets/tree3.png',
    ]
    trees = []

    position_function_list = [
        eval(
            'lambda t: (200 * t - x, y)',
            {
                'y': randrange(TREE_RANGE_HEIGHT[0], TREE_RANGE_HEIGHT[1]),
                'x': (tree_number * 25) + randrange(-VIDEO_SIZE[0], VIDEO_SIZE[0])
            }
        )
        for tree_number in range(count)
    ]

    for i in range(count):
        tree = mpy.ImageClip(random.choice(tree_paths), transparent=True). \
            set_position(position_function_list[i]). \
            resize(width=randrange(30, 50))
        trees.append(tree)
    return trees


ground_path = './assets/ground.jpg'
ground = mpy.ImageClip(ground_path, transparent=True). \
    set_position((0, -30)). \
    resize(width=VIDEO_SIZE[0])

video = mpy.CompositeVideoClip(
    [ground] + get_trees(DURATION * TREE_DENSITY) + [background],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(DURATION)
video.write_videofile('video.mp4', fps=25)
