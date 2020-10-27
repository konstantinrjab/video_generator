import moviepy.editor as mpy
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from random import randrange
import random
import math
import time
import os

VIDEO_SIZE = (480, 320)
TRAIN_SPEED = 200


def get_background():
    return mpy.ImageClip('./assets/background.png') \
        .set_position(('center', 0)) \
        .resize(width=VIDEO_SIZE[0])


def get_ground():
    return mpy.ImageClip('./assets/ground.jpg', transparent=True) \
        .set_position((0, -30)) \
        .resize(width=VIDEO_SIZE[0])


def get_filename(video_current_time: int):
    return 'video/' + str(video_current_time) + '.mp4'


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


video = InfVideoClip([get_ground()] + [get_background()], size=VIDEO_SIZE). \
    on_color(color=(255, 255, 255), col_opacity=1)

video_current_time = 0
duration = 5
clips = []
video_end_time = time.time()
buffer_time = 15

while True:
    if time.time() >= video_end_time - buffer_time:
        subclip = video.subclip(video_current_time, video_current_time + duration)
        filename = get_filename(video_current_time)
        subclip.write_videofile(filename, fps=25)
        clips.append(filename)

        video_current_time += duration
        video_end_time += duration
        if len(clips) > buffer_time / duration:
            os.remove(clips[0])
            del clips[0]
    else:
        print('sleep...')
        time.sleep(0.5)
