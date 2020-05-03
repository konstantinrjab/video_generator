import moviepy.editor as mpy
from random import randrange
import random

WHITE = (255, 255, 255)
VIDEO_SIZE = (640, 480)
DURATION = 5
TREE_RANGE_HEIGHT = (200, 300)

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
            'lambda t: (100 * t, m)',
            {'m': randrange(TREE_RANGE_HEIGHT[0], TREE_RANGE_HEIGHT[1])}
        )
        for m in range(count)
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
    [ground] + get_trees(5) + [background],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(DURATION)
video.write_videofile('video.mp4', fps=25)
