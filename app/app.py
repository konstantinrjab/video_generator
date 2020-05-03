import moviepy.editor as mpy
import gizeh

WHITE = (255, 255, 255)
VIDEO_SIZE = (640, 480)

background_path = './assets/background2.png'
background = mpy.ImageClip(background_path). \
    set_position(('center', 0)). \
    resize(width=VIDEO_SIZE[0])


def make_frame(t):
    surface = gizeh.Surface(width=VIDEO_SIZE[0], height=VIDEO_SIZE[1])
    line = gizeh.polyline(points=[(0, 100), (200, 300)], stroke_width=10, stroke=(1, 0, 0))
    line.draw(surface)
    return surface.get_npimage(transparent=True)


graphics_clip_mask = mpy.VideoClip(lambda t: make_frame(t)[:, :, 3] / 255.0, duration=5, ismask=True)
graphics_clip = mpy.VideoClip(lambda t: make_frame(t)[:, :, :3],
                              duration=5).set_mask(graphics_clip_mask)

video = mpy.CompositeVideoClip(
    [
        background,
        graphics_clip.set_position(
            ('center', 100)
        )
    ],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(5)

video.write_videofile('video.mp4', fps=10)
