# Import local library
import raytracer as rt


# Define some constants
WIDTH = 3
HEIGHT = 2


def main():
    """Creates a simple ppm image"""

    image = rt.Image(WIDTH, HEIGHT)

    # First row
    image.set_pixel(0, 0, rt.RED)
    image.set_pixel(1, 0, rt.GREEN)
    image.set_pixel(2, 0, rt.BLUE)

    # Second row
    image.set_pixel(0, 1, rt.RED + rt.GREEN)
    image.set_pixel(1, 1, rt.RED + rt.GREEN + rt.BLUE)
    image.set_pixel(2, 1, rt.RED * 0.001)

    # Write the image
    image.write_ppm()


if __name__ == '__main__':
    main()
