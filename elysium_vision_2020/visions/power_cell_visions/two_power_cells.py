from copy import copy

from elysium_vision_2020.visions.power_cell_visions.power_cell import *
from elysium_vision_2020.configurations import X_DIRECTION_LOCATION

two_power_cell_director = copy(one_power_cell_director)
two_power_cell = copy(one_power_cell)
two_power_cell_director.target_amount = 2
two_power_cell.director = two_power_cell_director

if __name__ == '__main__':
    POWER_CELL_VISION = two_power_cell
    power_cell_vision(POWER_CELL_VISION, X_DIRECTION_LOCATION)
