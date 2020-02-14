import ovl

TEAM_NUMBER = "1937"
NETWORK_TABLES_TABLE = "Vision"

UPDATE_KEY = "current_vision"
TARGET_X_KEY = "target_x"
TARGET_AMOUNT_KEY = "target_amount"

FEEDER_VISION_NAME = "feeder"
ONE_POWER_CELL_NAME = "ball_vision"
TWO_POWER_CELL_NAME = "two_balls"


CONTROLLER_UPDATE_LOCATION = ovl.NetworkLocation(table_key=UPDATE_KEY)
X_DIRECTION_LOCATION = ovl.NetworkLocation(table_key=TARGET_X_KEY)
TARGET_AMOUNT_LOCATION = ovl.NetworkLocation(table_key=TARGET_AMOUNT_KEY)
