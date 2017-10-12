# calling functions from outside

import random as rn
names = ["luca","Marco","Ali"]
volunteer = rn.choice(names)


import os
os.chdir("C:/Users/behzad/Dropbox/_2_Teaching Activities/_0_EETBS- On-going/EETBS 2017-2018 POLIMI-PIACENZA/3 Python Files and Guidelines")
import functionsCommands as FC

layers_wall = ["faceBreak_100mm","woodFiberboard_13mm"]
results=FC.wall_calc(layers_wall)