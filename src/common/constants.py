"""This file defines project-level constants."""
import numpy as np

MESSPUNKT_OBEN_LINKS = (890, 150)
MESSPUNKT_OBEN_RECHTS = (1000, 150)
MESSPUNKT_UNTEN_LINKS = (890, 500)
MESSPUNKT_UNTEN_RECHTS = (1000, 500)
SEITENLAENGE_MESSFLAECHE = 30


# Farbbereiche
LOWER_RED = np.array([0, 50, 50])
UPPER_RED = np.array([10, 255, 255])

LOWER_YELLOW = np.array([22, 93, 0])
UPPER_YELLOW = np.array([45, 255, 255])

LOWER_BLUE = np.array([110, 50, 50])
UPPER_BLUE = np.array([130, 255, 255])

LOWER_WHITE = np.array([0, 0, 168])
UPPER_WHITE = np.array([172, 111, 255])

LOWER_BLACK = np.array([0, 0, 0])
UPPER_BLACK = np.array([180, 255, 40])


# Ausrichtung Linienerkennung
LINE_THRESHOLD = 50         # minimum number of votes (intersections in Hough grid cell)
LINE_MIN_PX_LENGTH = 100    # minimum number of pixels making up a line
LINE_MAX_GAP = 40           # maximum gap in pixels between connectable line segments
