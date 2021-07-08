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

import os
import matplotlib.pyplot as plt

file_path = os.path.join(os.getcwd(), 'commonroad_io/commonroad/scenarios/NGSIM/Lankershim/USA_Lanker-1_1_T-1.xml')

scenario, planning_problem_set = CommonRoadFileReader(file_path).open()

# plt.figure(figsize=(25, 10))
# draw_object(scenario)
# draw_object(planning_problem_set)
# plt.gca().set_aspect('equal')
# plt.show()

print("[Log ERROR]:\033[1;31;23m red!\033[0m")
print("[Log WARNING]:\033[1;33;23m yellow!\033[0m")
print("[Log INFO]:\033[1;32;23mtgreen!\033[0m")