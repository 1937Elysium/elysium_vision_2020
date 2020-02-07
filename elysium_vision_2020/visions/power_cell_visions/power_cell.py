from ovl import *

from elysium_vision_2020.connections import *
from elysium_vision_2020.visions.power_cell_visions.two_power_cells import two_power_cell_director, two_power_cell

yellow = Color([22, 60, 60], [45, 255, 255])
contour_filters = [area_filter(min_area=200), dec_area_sort()]
image_filters = [ovl.gaussian_blur(kernel_size=(5, 5))]

one_power_cell_director = Director(directing_function=center_directions,
                                   target_amount=1,
                                   failed_detection=9999)

one_power_cell = Vision(camera=CAMERA,
                        threshold=yellow,
                        contour_filters=contour_filters,
                        image_filters=image_filters,
                        connection=ROBOT_NETWORK_TABLES_CONNECTION,
                        director=one_power_cell_director)


def power_cell_vision(power_cell, send_location):
    while True:
        image = power_cell.get_image()
        contours, _ = power_cell.detect(image)

        directions = power_cell.get_directions(contours, image)
        ovl.display_contours(image, delay=1, contours=contours)
        print("Directions:", directions)
        power_cell.send_to_location(directions, send_location)


if __name__ == '__main__':
    POWER_CELL_VISION = one_power_cell
    power_cell_vision(POWER_CELL_VISION, X_DIRECTION_LOCATION)
