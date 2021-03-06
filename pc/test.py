import time
import sys
import os
import platform

if sys.version_info[0] >= 3:
    print('Environment = Python 3 ---> Correct!')
else:
    try:
        print ('Environment = Python 2 ---> Incorrect!')
        print ('Environment testing fail, stop! ')
        exit()
    except:
        os.system('echo python2 error')
        exit()

if platform.system() != 'Linux':
    print('It is not Linux based system ---> Error')
    exit()


print()

print('Checking for Python toolkit...')

print('Checking for numpy')
try:
    import numpy as np
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install numpy before continuing")
    exit()

print('Checking for dlib')
try:
    import dlib as d
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install dlib before continuing")
    exit()


print('Checking for opencv')
try:
    import cv2 as c
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install opencv before continuing")
    exit()

print('Checking for skimage')
try:
    import skimage as s
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install skimage before continuing")
    exit()



print('Checking for platform')
try:
    import platform
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install platform before continuing")
    exit()


print('Checking for reload')
try:
    from imp import reload
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install reload before continuing")
    exit()


print('Checking for pickle')
try:
    import pickle
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install pickle before continuing")
    exit()


print('Checking for keras')
try:
    import keras
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install keras before continuing")
    exit()

print('Checking for face_recognition')
try:
    import face_recognition as fr
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install face_recognition before continuing")
    exit()



print('Checking for tensorflow')
try:
    import tensorflow as tf
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install tensorflow before continuing")
    exit()

print('Checking for sklearn')
try:
    from sklearn import datasets, svm, metrics
    print('---> Correct!')
except ImportError:
    print('---> Error!')
    print("you should install imageio before continuing")
    exit()


print()
print()

print('Checking Python toolkit finished !')

print('Congratulation, you are ready to go!')