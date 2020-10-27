import moviepy.editor as mpy
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from random import randrange
import random
import datetime
import math

VIDEO_SIZE = (480, 320)
TRAIN_SPEED = 200


class InfVideoClip(CompositeVideoClip):
    tree_paths = [
        './assets/tree1.png',
        './assets/tree2.png',
        './assets/tree3.png',
    ]
    processed_second = 0
    clips_on_top_layer_count = 1
    clips_on_bottom_layer_count = 1

    def get_frame(self, t: float):
        current_second = math.floor(t)

        if self.processed_second != current_second:
            self.processed_second = current_second
            y = randrange(100, 200)
            tree = mpy.ImageClip(random.choice(self.tree_paths), transparent=True). \
                set_position(lambda t: (t * TRAIN_SPEED - current_second * TRAIN_SPEED, y)). \
                resize(width=randrange(30, 50))
            self.clips.insert(len(self.clips) - self.clips_on_top_layer_count, tree)
            if len(self.clips) > 10:
                del self.clips[self.clips_on_bottom_layer_count]
        return super().get_frame(t)


def get_background():
    return mpy.ImageClip('./assets/background.png') \
        .set_position(('center', 0)) \
        .resize(width=VIDEO_SIZE[0])


def get_ground():
    return mpy.ImageClip('./assets/ground.jpg', transparent=True) \
        .set_position((0, -30)) \
        .resize(width=VIDEO_SIZE[0])


video = InfVideoClip([get_ground()] + [get_background()], size=VIDEO_SIZE). \
    on_color(color=(255, 255, 255), col_opacity=1)


time = 0
duration = 8
folder = 'video/'
counter = 0
while counter < 1:
    subclip = video.subclip(time, time + duration)

    filename = datetime.datetime.now().strftime('%H-%M-%S') + '.mp4'
    subclip.write_videofile(folder + filename, fps=25)
    time += duration
    counter += 1
