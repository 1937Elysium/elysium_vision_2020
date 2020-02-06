import cv2
import platform

from elysium_vision_2020.configurations import *

ROBOT_NETWORK_TABLES_CONNECTION = ovl.NetworkTablesConnection(TEAM_NUMBER, table_name=NETWORK_TABLES_TABLE)
CAMERA_PORT = 1 if platform.system() == "Windows" else 0
CAMERA = cv2.VideoCapture(CAMERA_PORT)
