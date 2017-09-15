# 1.0 - Acer 2017/09/15 14:49

from VrepPythonApi import vrep
from VrepPythonApi import vrep_ext
import os


# ============================================================================ #
#                                  Start VREP                                  #
# ============================================================================ #
path_vrep = '"C:\\Program Files\\V-REP3\V-REP_PRO\\vrep.exe"'
os.startfile(path_vrep)


# ============================================================================ #
#                               Connect to V-REP                               #
# ============================================================================ #
v = vrep_ext.VrepController()


# ============================================================================ #
#                 Load ScriptDummy.py demo scene by remote API                 #
# ============================================================================ #
path_scene = os.path.join(os.getcwd(), 'vrep_ext_demo.ttt')
vrep.simxLoadScene(v.clientID, path_scene, 0, vrep.simx_opmode_blocking)


# ============================================================================ #
#                               Start simulation                               #
# ============================================================================ #
v.startSim()


# ============================================================================ #
#                      Call build-in regular API function                      #
# ============================================================================ #
# create a cubic objects
h_cube = v.callBuildinFunction('simCreatePureShape', vrep.simx_opmode_blocking,
                               '0', '8', '{0.1, 0.1, 0.1}', '1')[1]


# ============================================================================ #
#                           Call child scrip function                          #
# ============================================================================ #
# call a function "showPopUpMessage" which is associated with "ScriptDummy" object
#
# Notice that the input argument "Hello World" is a string in VREP Lua script.
# Therefore, we need to create "a string in a string" for this argument
v.callAssociatedScriptFunction('ScriptDummy', 'showPopUpMessage', vrep.simx_opmode_blocking, '"Hello World"')


# ============================================================================ #
#                                      End                                     #
# ============================================================================ #
v.stopSim()
