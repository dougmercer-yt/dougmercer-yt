import taichi as ti

ti.init(arch=ti.gpu)

n = 1920

res = (3840, 2160)
pixels = ti.field(dtype=float, shape=res)


@ti.func
def complex_sqr(z):
    return ti.Vector([z[0] ** 2 - z[1] ** 2, z[1] * z[0] * 2])


@ti.kernel
def paint(t: float):
    for i, j in pixels:  # Parallelized over all pixels
        c = ti.Vector([-0.8, ti.cos(t) * 0.2])
        z = ti.Vector([i / n - 1, j / n - 0.6]) * 2.5
        iterations = 0
        while z.norm() < 20 and iterations < 50:
            z = complex_sqr(z) + c
            iterations += 1
        pixels[i, j] = 1 - iterations * 0.02

live_viz = True
if live_viz:
    # gui = ti.GUI("Julia Set", res=(n * 2, n))
    window = ti.ui.Window(name="Julia Set", res=res, fps_limit=400, pos = (150, 150))
    canvas = window.get_canvas()

    for i in range(1000000):
        paint(i * 0.03)
        canvas.set_image(pixels)
        window.show()
        # canvas.show()
else:
    result_dir = "./results"
    video_manager = ti.tools.VideoManager(output_dir=result_dir, framerate=24, automatic_build=False)

    for i in range(240):
        paint(i * 0.09)
        pixels_img = pixels.to_numpy()
        video_manager.write_frame(pixels_img)

    video_manager.make_video(gif=False, mp4=True)
