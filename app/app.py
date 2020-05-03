import moviepy.editor as mpy
from random import randrange
import random

VIDEO_SIZE = (640, 480)
DURATION = 8
TREE_Y_RANGE = (250, 320)
TREE_DENSITY = 100
TREE_DISTANCE_BETWEEN = 50
TRAIN_SPEED = 75

WHITE = (255, 255, 255)


def get_background():
    return mpy.ImageClip('./assets/background.png') \
        .set_position(('center', 0)) \
        .resize(width=VIDEO_SIZE[0])


def get_ground():
    return mpy.ImageClip('./assets/ground.jpg', transparent=True) \
        .set_position((0, -30)) \
        .resize(width=VIDEO_SIZE[0])


def get_trees():
    tree_paths = [
        './assets/tree1.png',
        './assets/tree2.png',
        './assets/tree3.png',
    ]
    trees = []
    trees_count = DURATION + round(VIDEO_SIZE[0] / TRAIN_SPEED)
    position_function_list = [
        eval(
            'lambda t: (t * speed + x, y)',
            {
                'y': randrange(TREE_Y_RANGE[0], TREE_Y_RANGE[1]),
                'speed': TRAIN_SPEED,
                'x': (tree_number * TREE_DISTANCE_BETWEEN) - VIDEO_SIZE[0]
            }
        )
        for tree_number in range(trees_count)
    ]

    for i in range(trees_count):
        tree = mpy.ImageClip(random.choice(tree_paths), transparent=True). \
            set_position(position_function_list[i]). \
            resize(width=randrange(30, 50))
        trees.append(tree)
    return trees


video = mpy.CompositeVideoClip(
    [get_ground()] + get_trees() + [get_background()],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(DURATION)
video.write_videofile('video.mp4', fps=25)
