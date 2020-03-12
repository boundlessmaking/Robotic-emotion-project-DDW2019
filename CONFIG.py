import math
import sys
from PROGRAMSTATE import ProgramState

RASPBERRY_BOOL = False
if sys.platform == "linux":
    RASPBERRY_BOOL = True
    import picamera
    from picamera.array import PiRGBArray

PROGRAMSTATE = ProgramState() 
ROBOT_ACTION = 0

#ROBOT_IP = "10.211.55.5"
ROBOT_IP = "192.168.178.35"

FACE_ACTIVATE = True
FACE_ROW_OFFSET = [0, 0.01]
TEXT_HOR_OFFSET = 0.04
Z_HOP = 0.006
DRAWING_ZVAL = 0.015
CURRENT_ROW = 0
MAX_ROWS = 5
ROW_SPACING = 0.06
LINE_SPACING = 0.012
BLEND_RADIUS = 0.0005
TEXT_SCALING = 1/120
LETTER_SPACING = 0.006

MAX_X = 0.2
MAX_Y = 0.2
HOR_ROT_MAX = math.radians(50)
VERT_ROT_MAX = math.radians(25)
ACCEL = 0.1
VEL= 0.5


FOLLOW_TIME = 20
WANDER_DIST = 0.003
W_ANGLECHANGE = 5.0
ESCAPE_ANGLECHANGE = 45

# reporting
PRINT_COORDINATES = False
SHOW_FRAME = True

# self.face_detect = dlib.get_frontal_face_detector()
#dnnFaceDetector = dlib.cnn_face_detection_model_v1("models/mmod_human_face_detector.dat")
# paper advancing
DRAG_DIST = 0.14  # 10 cm
#PLUNGE_DIST = 0.1273
PLUNGE_DIST = 0.072
PAPERSLOT_START = [-0.075, -0.548, 0.1980, 0.0, -3.14, 0]

# positions
HOME_POS = (math.radians(180),
                 math.radians(-90),
                 math.radians(-101.5),
                 math.radians(-19),
                 math.radians(88),
                 math.radians(0))

ABOVE_PAPER = (math.radians(22),
                 math.radians(-107.2),
                 math.radians(-113.5),
                 math.radians(-48.7),
                 math.radians(90.4),
                 math.radians(21.75))

BETWEEN = (math.radians(27),
                 math.radians(-57.5),
                 math.radians(-117.6),
                 math.radians(-89.6),
                 math.radians(90),
                 math.radians(17.6))




VIDEO_RESOLUTION = (640, 480)  # resolution the video capture will be resized to, smaller sizes can speed up detection
VIDEO_MIDPOINT = (int(VIDEO_RESOLUTION[0]/2),
                  int(VIDEO_RESOLUTION[1]/2))
VIDEO_ASPECT_RATIO  = VIDEO_RESOLUTION[0] / VIDEO_RESOLUTION[1]  # Aspect ration of each frame
VIDEO_VIEWANGLE_HOR = math.radians(25)  # Camera FOV (field of fiew) angle in radians in horizontal direction
#video_viewangle_vert = video_viewangle_hor / video_asp_ratio  #  Camera FOV (field of fiew) angle in radians in vertical direction
M_PER_PIXEL = 00.00004  # Variable which scales the robot movement from pixels to meters.

# LED Pins: 
# Led colour pins
