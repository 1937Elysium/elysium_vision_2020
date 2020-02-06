import ovl
from ..configurations import *

visions = []

vision_controller = ovl.MultiVision(update_connection=ROBOT_NETWORK_TABLES_CONNECTION,
                                    update_location=CONTROLLER_UPDATE_LOCATION,
                                    vision_list=visions)

if __name__ == '__main__':
    for directions, contours, filtered_image in vision_controller.start():
        pass


