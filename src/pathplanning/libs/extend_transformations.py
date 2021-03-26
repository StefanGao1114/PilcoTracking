import numpy as np
from numpy.linalg import inv
import math
from .transformations import *

def getYawRightRange(yaw) :
    if yaw > np.pi or yaw < -np.pi :
        yaw = np.arctan2(np.sin(yaw), np.cos(yaw))
    return yaw

def minusPi_to_pi(angle) :
    if angle > math.pi or angle < -math.pi :
        return math.atan2(math.sin(angle), math.cos(angle))
    else :
        return angle

def yaw_to_quaternion(yaw) :
    return euler_to_quaternion(0.0, 0.0, yaw)

def translation_quaternion_to_matrix(translation, quaternion) :
    translation_matrix = translation_to_matrix(translation)
    '''
    translation_m = [1.,0.,0.,x
                     0.,1.,0.,y
                     0.,0.,1.,0.0
                     0.,0.,0.,1.]
    '''
    quaternion_matrix = quaternion_to_matrix(quaternion)
    matrix = quaternion_matrix
    matrix[:3,3] = translation_matrix[:3,3]
    '''
    matrix = [[Rotations], x 
                           y
               matrix ]    0.0
                0.,0.,0.,  1.]
    '''
    return matrix



def xyYaw_to_matrix(*args, **kwargs) :
    if len(args) == 1: # For Tuple
        # print("asd--------------_>")
        x = args[0][0]
        y = args[0][1]
        yaw = args[0][2]
    elif len(args) == 3:
        x = args[0]
        y = args[1]
        yaw = args[2]
    elif len(kwargs) == 3:
        x = kwargs["x"]
        y = kwargs["y"]
        yaw = kwargs["yaw"]
    translation = [x, y, 0.0]
    rotation = yaw_to_quaternion(yaw)
    matrix = translation_quaternion_to_matrix(translation, rotation)
    return matrix

def getLength2D(first, second):
    if type(first).__name__ == "tuple" and type(second).__name__ == "tuple":
        dx = first[0] - second[0]
        dy = first[1] - second[1]
        dL = np.hypot(dx, dy)
        return dL
    else:
        print("HAS TO BE DEFINED")
    

def getLength2DSign(first, second) :
    if type(first) is np.ndarray and type(second) is np.ndarray :
        first2second = np.matmul(np.linalg.inv(first), second)
        # print "first2second:\n", first2second
        delta_position = np.asarray( [first2second[0, 3], first2second[1, 3] ])
        delta_length = np.linalg.norm(delta_position) * np.sign(delta_position[0])
        return delta_length
    else :
        print("Error in getLength: Datatypes are not equal or unknown")

def getLength(first, second) :
    if type(first) is np.ndarray and type(second) is np.ndarray :
        first2second = np.matmul(np.linalg.inv(first), second)
        delta_position = np.asarray( [first2second[0, 3], first2second[1, 3], first2second[2, 3] ])
        delta_length = np.linalg.norm(delta_position)
        return delta_length
    else :
        print("Error in getLength: Datatypes are not equal or unknown")



def matrix_to_translation_quaternion(matrix) :
    quaternion = matrix_to_quaternion(matrix)
    translation = matrix_to_translation(matrix)
    return translation, quaternion

def matrix_to_translation_euler(matrix) :
    roll, pitch, yaw = matrix_to_euler(matrix)
    translation = matrix_to_translation(matrix)
    return translation, [roll, pitch, yaw]


def matrix_to_yaw(matrix) :
    _, _, yaw = matrix_to_euler(matrix)
    return yaw

def yaw_to_matrix(yaw) :
    return euler_to_matrix(0.0, 0.0, yaw)

def tfMatrix_to_positionEulerNpArray(tf_matrix) :
    position = matrix_to_translation(tf_matrix)
    R, P, Y = matrix_to_euler(tf_matrix)
    positionEulerNpArray = np.array( [position[0], position[1], position[2], R, P, Y ] )
    return positionEulerNpArray

def tfMatrix_to_xyYawNpArray(tf_matrix) :
    positionEuler = tfMatrix_to_positionEulerNpArray(tf_matrix)
    xyYaw = np.array( [positionEuler[0], positionEuler[1], positionEuler[5]] )
    return xyYaw









if __name__ == "__main__":
    
    print ("getYawRightRange = ", getYawRightRange(4.2))
    print ("minusPi_to_pi = ", minusPi_to_pi(4.2))

    print("yaw_to_quaternion = ", yaw_to_quaternion(1.0))
    quat = yaw_to_quaternion(-1.4);
    trans = [14.0, 444.0, 44.04  ]
    print("translation_quaternion_to_matrix:\n", translation_quaternion_to_matrix(trans, quat))
    print("xyYaw_to_matrix:\n", xyYaw_to_matrix(x=0.1, y=0.6, yaw=1.0))

    print("getLength2DSign = ", getLength2DSign(xyYaw_to_matrix(x=0.1, y=0.6, yaw=1.0), xyYaw_to_matrix(x=-11.1, y=2.6, yaw=-2.3)) )
    print("getLength = ", getLength(xyYaw_to_matrix(x=0.1, y=0.6, yaw=1.0), xyYaw_to_matrix(x=-11.1, y=2.6, yaw=-2.3)) )

    test_matrix = translation_quaternion_to_matrix(trans, quat)
    print("matrix_to_translation_quaternio:\n", matrix_to_translation_quaternion(test_matrix))
    print("quaternion_to_euler= ", quaternion_to_euler(quat))

    print("matrix_to_translation_euler = ", matrix_to_translation_euler(test_matrix))

    print("matrix_to_yaw = ", matrix_to_yaw(test_matrix))

    print("yaw_to_matrix = ", yaw_to_matrix(-3.0))

    print("tfMatrix_to_positionEulerNpArray = ", tfMatrix_to_positionEulerNpArray(test_matrix))
    print("tfMatrix_to_xyYawNpArray = ", tfMatrix_to_xyYawNpArray(test_matrix))