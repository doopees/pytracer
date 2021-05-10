# Import local libraries
import raytracer as rt


# Define some constants
WIDTH = 320
HEIGHT = 200


def main():
    # Initialize the scene
    scene = rt.Scene()

    # Setup the scene
    scene.set_camera(
        rt.Point([0, 0, -1])
    )
    scene.add_objects(
        rt.Sphere(rt.ORIGIN,
                  0.3,
                  rt.Material(rt.Color.from_hex('#990000'))
        ),
        rt.Sphere(rt.Point([0.1, 0.1, -0.5]),
                  0.1,
                  rt.Material(rt.Color.from_hex('#00E5EE'))
        )
    )
    scene.add_lights(
        rt.Light(rt.Point([-1.5, -0.5, -10]), rt.WHITE)
    )

    # Render the image
    image = scene.render(WIDTH, HEIGHT)

    # Write the image to a ppm file
    image.write_ppm()


if __name__ == '__main__':
    main()
