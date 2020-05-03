import moviepy.editor as mpy

WHITE = (255, 255, 255)
VIDEO_SIZE = (640, 480)

background_path = './assets/background.png'
background = mpy.ImageClip(background_path). \
    set_position(('center', 0)). \
    resize(width=VIDEO_SIZE[0])

tree_path = './assets/tree1.png'
tree = mpy.ImageClip(tree_path, transparent=True). \
    set_position(lambda t: (t * 100, 250)). \
    resize(width=30)

ground_path = './assets/ground.jpg'
ground = mpy.ImageClip(ground_path, transparent=True). \
    set_position((0, -30)). \
    resize(width=VIDEO_SIZE[0])

video = mpy.CompositeVideoClip(
    [
        ground,
        tree,
        background
    ],
    size=VIDEO_SIZE). \
    on_color(
    color=WHITE,
    col_opacity=1).set_duration(5)
video.write_videofile('video.mp4', fps=25)
