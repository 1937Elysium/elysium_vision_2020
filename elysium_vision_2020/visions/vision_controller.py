from ..configurations import *

visions = []

vision_controller = ovl.MultiVision(update_connection=ROBOT_NETWORK_TABLES_CONNECTION,
                                    update_location=CONTROLLER_UPDATE_LOCATION,
                                    vision_list=visions)
