# pip install numpy
# pip install pandas
# pip install pyplot
# pip install matplotlib
# pip list
# pip show selenium

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url1='https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
lpd = pd.read_csv(url1)
lpd.plot()
plt.show()