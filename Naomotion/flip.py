
import sys
import motion
from naoqi import ALProxy
#import virtkey
import almath
import webbrowser
import time






#time.sleep(1)
#webbrowser.open("https://bright626816.github.io/")
try:

names = list()
times = list()
keys = list()
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "169.254.137.199", 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)

names.append("LElbowRoll")
times.append([0, 1.56, 2.56, 3.56])
keys.append([-0.0413762, -0.325165, -0.395731, -0.167164])

names.append("LElbowYaw")
times.append([0, 1.56, 2.56, 3.56])
keys.append([-0.745566, -1.17969, -1.19503, -0.790051])

names.append("LHand")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.0296, 0.304, 0.2904, 0.0748])

names.append("LShoulderPitch")
times.append([0, 1.56, 2.56, 3.56])
keys.append([1.48334, 1.52169, 1.50021, 1.32687])

names.append("LShoulderRoll")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.202446, 0.0797259, 0.154892, -0.0153821])

names.append("LWristYaw")
times.append([0, 1.56, 2.56, 3.56])
keys.append([-0.817664, 0.0981341, 0.0843279, -0.753235])

names.append("RElbowRoll")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.030722, 1.51563, 1.44967, 0.165714])

names.append("RElbowYaw")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.837522, 2.08926, 0.67952, 0.993989])

names.append("RHand")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.0384001, 0.852, 0.314, 0.092])

names.append("RShoulderPitch")
times.append([0, 1.56, 2.56, 3.56])
keys.append([1.55245, 0.546147, 0.737896, 1.35456])

names.append("RShoulderRoll")
times.append([0, 1.56, 2.56, 3.56])
keys.append([-0.159578, -0.285367, 0.329768, -0.0245859])

names.append("RWristYaw")
times.append([0, 1.56, 2.56, 3.56])
keys.append([0.673385, -0.135034, -0.0844118, 0.435615])


except BaseException, err:
  print err
#time.sleep(1.56)
#v=virtkey.virtkey()
#v.press_keysym(65363)
#v.release_keysym(65363)

