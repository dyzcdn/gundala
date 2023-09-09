import threading
import numpy
from PIL import Image
from keras import Model

from roop.typing import Frame

THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.85