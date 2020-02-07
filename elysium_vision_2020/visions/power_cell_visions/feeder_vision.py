from ovl import *

from elysium_vision_2020.connections import *
from elysium_vision_2020.configurations import *

green = Color([35, 70, 70], [75, 255, 255])
filters = [area_filter(), dec_area_sort()]
image_filters = [gaussian_blur(kernel_size=(5, 5), sigma_x=5)]

feeder_director = Director(directing_function=center_directions,
                           target_amount=1,
                           failed_detection=9999)

feeder_vision = Vision(camera=CAMERA,
                       threshold=green,
                       contour_filters=filters,
                       image_filters=image_filters,
                       connection=ROBOT_NETWORK_TABLES_CONNECTION,
                       director=feeder_director)

if __name__ == '__main__':
    CAMERA.set(15, -11)
    while True:
        image = feeder_vision.get_image()
        contours, _ = feeder_vision.detect(image)

        directions = feeder_vision.get_directions(contours, image)
        ovl.display_contours(image, delay=1, contours=contours)
        print("Directions:", directions)
        feeder_vision.send_to_location(directions, send_location)
