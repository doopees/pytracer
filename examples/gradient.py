import raytracer as rt


WIDTH = 200
HEIGHT = 100
COLOR = rt.Color([0.5, 0.7, 1.0])


def get_color(ray):
    t = ray.direction.normalize().y
    return t*rt.WHITE + (1-t)*COLOR


def main():
    # 2D scene
    lower_left_corner = rt.Point([-2, 0, -1])
    horizontal = rt.Vector([4, 0, 0])
    vertical = rt.Vector([0, 2, 0])

    camera = rt.Point([0, 0, 0])
    image = rt.Image(WIDTH, HEIGHT)

    for i in range(WIDTH):
        for j in range(HEIGHT):
            u = i / WIDTH
            v = j / HEIGHT
            point = lower_left_corner + u*horizontal + v*vertical
            ray = rt.Ray.from_points(camera, point)
            color = get_color(ray)
            image.set_pixel(i, j, color)

    image.write_ppm()


if __name__ == '__main__':
    main()
