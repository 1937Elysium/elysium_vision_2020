from elysium_vision_2020.visions.vision_controller import vision_controller
from elysium_vision_2020.configurations import VISION_TO_NETWORK_LOCATION

if __name__ == '__main__':
    for directions, contours, filtered_image in vision_controller.start():
        network_location = VISION_TO_NETWORK_LOCATION[vision_controller]
        vision_controller.current.send_to_location(directions, network_location=network_location)
