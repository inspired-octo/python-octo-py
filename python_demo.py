from commonroad_io.commonroad import common
from commonroad_io.commonroad.common.file_reader import CommonRoadFileReader
import os
import time
import requests
import pandas as pd
from pprint import pprint
from lxml import etree
import time
import warnings
warnings.filterwarnings("ignore")
from IPython import display

import os
import matplotlib.pyplot as plt
from commonroad_io.commonroad.visualization.draw_dispatch_cr import draw_object

# file_path = os.path.join(os.getcwd(), 'commonroad-scenarios/scenarios/NGSIM/Lankershim/USA_Lanker-1_1_T-1.xml')

# scenario, planning_problem_set = CommonRoadFileReader(file_path).open()

# plt.figure(figsize=(25, 10))
# draw_object(scenario)
# # draw_object(planning_problem_set)
# plt.gca().set_aspect('equal')
# plt.show()
file_path = '/Users/shifei/Desktop/octo-rupin/python-octo-py/commonroad-scenarios/scenarios/interactive/hand-crafted/ZAM_Tutorial-1_1_I-1-1/ZAM_Tutorial-1_1_I-1-1.cr.xml'


# read in the scenario and planning problem set
scenario, planning_problem_set = CommonRoadFileReader(file_path).open()

# plot the scenario for 40 time step, here each time step corresponds to 0.1 second
for i in range(0, 40):
    # uncomment to clear previous graph
    # display.clear_output(wait=True)
    
    plt.figure(figsize=(20, 10))
    # plot the scenario at different time step
    draw_object(scenario, draw_params={'time_begin': i})
    # plot the planning problem set
    draw_object(planning_problem_set)
    plt.gca().set_aspect('equal')
    plt.show()

print("[Log ERROR]:\033[1;31;23m red!\033[0m")
print("[Log WARNING]:\033[1;33;23m yellow!\033[0m")
print("[Log INFO]:\033[1;32;23mtgreen!\033[0m")