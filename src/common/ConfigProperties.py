"""This file defines project-level constants."""
import os
import numpy as np

class ConfigProperties:
    __instance = None

    # Environment
    DEPLOY_ENV = os.getenv("DEPLOY_ENV")
    DEPLOY_ENV_PROD = True if DEPLOY_ENV == "prod" else False
    DEPLOY_PORT = os.getenv("PORT")

    # Farberkennung
    MESSPUNKT_OBEN_LINKS = (190, 10)
    MESSPUNKT_OBEN_RECHTS = (250, 10)
    MESSPUNKT_UNTEN_LINKS = (190, 150)
    MESSPUNKT_UNTEN_RECHTS = (250, 150)
    SEITENLAENGE_MESSFLAECHE = 15

    # Camera/Frame Region of Interest
    ROI_UPPER_LEFT = (100, 50)
    ROI_BOTTOM_RIGHT = (510, 350)

    # Farbbereiche
    LOWER_RED = np.array([30, 25, 104])
    UPPER_RED = np.array([68, 63, 288])

    LOWER_YELLOW = np.array([3, 142, 116])
    UPPER_YELLOW = np.array([23, 162, 196])

    LOWER_BLUE = np.array([132, 58, -15])
    UPPER_BLUE = np.array([258, 119, 50])

    LOWER_WHITE = np.array([0, 0, 168])
    UPPER_WHITE = np.array([172, 111, 255])

    LOWER_BLACK = np.array([0, 0, 0])
    UPPER_BLACK = np.array([180, 255, 40])

    # Ausrichtung Linienerkennung
    LINE_THRESHOLD = 50                     # minimum number of votes (intersections in Hough grid cell)
    LINE_MIN_PX_LENGTH = 100                # minimum number of pixels making up a line
    LINE_MAX_GAP = 40                       # maximum gap in pixels between connectable line segments

    ANGLE_DEVIATION_THRESHOLD_DEG = 2       # How much the vertical or horizontal line is allowed to deviate. (±)
    DETECT_FRAMES_COUNT: int = 4            # Maximal count of aligned frames to be detected and returned.
    DETECT_FRAMES_STEP: int = 90
    MAX_ANGLE_ROTATION_FIRST_FRAME = 95
    TURNTABLE_RPM = 2.3                       # Turntable rotation speed given as rotations per minute. Specified in PREN is 2rpm (12°/s). -> Real RPM deviates!

    # API & RTSP Konfiguration
    RTSP_IP = "147.88.48.131:554" if DEPLOY_ENV_PROD else "147.88.48.131:554"
    RTSP_PATH = "/axis-media/media.amp"
    RTSP_URL = RTSP_IP + RTSP_PATH
    RTSP_USERNAME = "pren"
    RTSP_PASSWORD = "463997"
    RTSP_PROFILE = "pren_profile_small"     # "pren_profile_small" or "pren_profile_med"

    # Ausrichtung Linienerkennung
    DEBUG_SHOW_LIVESTREAM = True
    DEBUG_SHOW_WHITE_MASK = False
    DEBUG_SHOW_CONTOUR = False
    DEBUG_SHOW_HOUGH_LINES = True
    DEBUG_SHOW_DETECTED_FRAME = True
    DEBUG_SHOW_COLOR_PICKER = False
    DEBUG_SHOW_COLOR_MASK = False

    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super(ConfigProperties, cls).__new__(cls)
            cls.__instance.reset()
    
        return cls.__instance
    
    def reset(self):
        self.DEPLOY_ENV = os.getenv("DEPLOY_ENV")
        self.DEPLOY_ENV_PROD = True if self.DEPLOY_ENV == "prod" else False
        self.DEPLOY_PORT = os.getenv("PORT")
        self.MESSPUNKT_OBEN_LINKS = (190, 10)
        self.MESSPUNKT_OBEN_RECHTS = (250, 10)
        self.MESSPUNKT_UNTEN_LINKS = (190, 150)
        self.MESSPUNKT_UNTEN_RECHTS = (250, 150)
        self.SEITENLAENGE_MESSFLAECHE = 15
        self.ROI_UPPER_LEFT = (100, 50)
        self.ROI_BOTTOM_RIGHT = (510, 350)
        self.LOWER_RED = np.array([30, 25, 104])
        self.UPPER_RED = np.array([68, 63, 288])
        self.LOWER_YELLOW = np.array([60, 175, 183])
        self.UPPER_YELLOW = np.array([23, 213, 220])
        self.LOWER_BLUE = np.array([108, 47, -13])
        self.UPPER_BLUE = np.array([258, 119, 50])
        self.LOWER_WHITE = np.array([0, 0, 168])
        self.UPPER_WHITE = np.array([172, 111, 255])
        self.LOWER_BLACK = np.array([0, 0, 0])
        self.UPPER_BLACK = np.array([180, 255, 40])
        self.LINE_THRESHOLD = 50 
        self.LINE_MIN_PX_LENGTH = 100 
        self.LINE_MAX_GAP = 40 
        self.ANGLE_DEVIATION_THRESHOLD_DEG = 2 
        self.DETECT_FRAMES_COUNT: int = 4
        self.DETECT_FRAMES_STEP: int = 90
        self.MAX_ANGLE_ROTATION_FIRST_FRAME = 95
        self.TURNTABLE_RPM = 2.3
        self.RTSP_IP = "147.88.48.131:554" if self.DEPLOY_ENV_PROD else "147.88.48.131:554"
        self.RTSP_PATH = "/axis-media/media.amp"
        self.RTSP_URL = self.RTSP_IP + self.RTSP_PATH
        self.RTSP_USERNAME = "pren"
        self.RTSP_PASSWORD = "463997"
        self.RTSP_PROFILE = "pren_profile_small"     # "pren_profile_small" or "pren_profile_med"
        self.DEBUG_SHOW_LIVESTREAM = True
        self.DEBUG_SHOW_WHITE_MASK = False
        self.DEBUG_SHOW_CONTOUR = False
        self.DEBUG_SHOW_HOUGH_LINES = True
        self.DEBUG_SHOW_DETECTED_FRAME = True
        self.DEBUG_SHOW_COLOR_PICKER = False
        self.DEBUG_SHOW_COLOR_MASK = False