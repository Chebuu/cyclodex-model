
import numpy as np
from scipy.spatial.transform import Rotation

def flip_positions(positions):
    posNP = np.array(positions._value)
    rot180 = Rotation.from_quat([0, 0, np.sin(np.pi/2), np.cos(np.pi/2)])
    rot180.apply(posNP)