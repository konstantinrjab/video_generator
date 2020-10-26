import moviepy.editor as mpy
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from random import randrange
import random
import datetime
import math


class InfVideoClip(CompositeVideoClip):
    tree_paths = [
        './assets/tree1.png',
        './assets/tree2.png',
        './assets/tree3.png',
    ]
    processed_second = 0
    clips_init_count = None

    def get_frame(self, t):
        if self.clips_init_count is None:
            self.clips_init_count = len(self.clips)
        current_second = math.floor(t)

        if self.processed_second != current_second:
            self.processed_second = current_second
            y = randrange(100, 200)
            tree = mpy.ImageClip(random.choice(self.tree_paths), transparent=True). \
                set_position(lambda t: (t * TRAIN_SPEED - current_second * TRAIN_SPEED, y)). \
                resize(width=randrange(30, 50))
            self.clips.append(tree)
            if len(self.clips) > 10:
                self.clips.pop(self.clips_init_count)
                # del self.clips[-1]
        return super().get_frame(t)


VIDEO_SIZE = (480, 320)
TREE_Y_RANGE = (250, 320)
TREE_DENSITY = 100
TREE_DISTANCE_BETWEEN = 50
TRAIN_SPEED = 200

WHITE = (255, 255, 255)


def get_background():
    return mpy.ImageClip('./assets/background.png') \
        .set_position(('center', 0)) \
        .resize(width=VIDEO_SIZE[0])


def get_ground():
    return mpy.ImageClip('./assets/ground.jpg', transparent=True) \
        .set_position((0, -30)) \
        .resize(width=VIDEO_SIZE[0])

video = InfVideoClip(
    [get_ground()] + [get_background()],
    # [get_ground()],
    size=VIDEO_SIZE
    ). \
    on_color(color=WHITE, col_opacity=1)

time = 0
duration = 20
folder = 'video/'
counter = 0
while counter < 1:
    subclip = video.subclip(time, time + duration)

    now = datetime.datetime.now()
    filename = str(now.hour) + str(now.minute) + str(now.second) + '.mp4'
    subclip.write_videofile(folder + filename, fps=25)
    time += duration
    counter += 1
