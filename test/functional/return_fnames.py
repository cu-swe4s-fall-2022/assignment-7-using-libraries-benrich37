import os
import sys
mainpath = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(mainpath)
import plotter
print(str(plotter.fname1) +
      ' ' + str(plotter.fname2) +
      ' ' + str(plotter.fname3))
