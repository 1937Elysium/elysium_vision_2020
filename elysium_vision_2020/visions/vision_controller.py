from elysium_vision_2020.connections import *
from elysium_vision_2020.visions.power_cell_visions.power_cell import one_power_cell
from elysium_vision_2020.visions.power_cell_visions.feeder_vision import feeder_vision
from elysium_vision_2020.visions.power_cell_visions.two_power_cells import two_power_cell
from elysium_vision_2020.configurations import *

visions = {FEEDER_VISION_NAME: feeder_vision,
           ONE_POWER_CELL_NAME: one_power_cell,
           TWO_POWER_CELL_NAME: two_power_cell}

vision_controller = ovl.MultiVision(update_connection=ROBOT_NETWORK_TABLES_CONNECTION,
                                    update_location=CONTROLLER_UPDATE_LOCATION,
                                    vision_list=visions,
                                    default_vision="feeder")
