import moviepy.editor as mpy
import gizeh as gz
from math import pi

BLUE = (59 / 255, 89 / 255, 152 / 255)
WHITE = (255, 255, 255)
VIDEO_SIZE = (640, 480)


def draw_stars(t):
    surface = gz.Surface(640, 120)

    for i in range(5):
        star = gz.star(nbranches=5, radius=120 * 0.2,
                       xy=[100 * (i + 1), 50], fill=(0, 1, 0),
                       angle=t * pi)
        star.draw(surface)
    return surface.get_npimage()


background_path = './assets/background2.png'
background = mpy.ImageClip(background_path). \
    set_position(('center', 0)). \
    resize(width=VIDEO_SIZE[0])

stars = mpy.VideoClip(draw_stars, duration=5)

video = mpy.CompositeVideoClip(
    [
        background,
        stars.set_position(
            ('center', 100)
        )
    ],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(5)

video.write_videofile('video.mp4', fps=10)
