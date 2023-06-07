import numpy as np
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
import subprocess
import time
from datetime import datetime
from PIL import Image
run = 1
starttime = datetime.now()
present_dir = os.getcwd()
def root_path():
	return os.path.abspath(os.sep)

samples = ["n_grid-500-CL-736x622",
	   "n_grid-500-CL-736x622-alt1",
	   "n_grid-500-CL-736x622-alt2",
	   "n_grid-1500-CL-736x622",
	   "n_grid-1500-CL-736x622-alt1",
	   "n_grid-1500-CL-736x622-alt2"]

for loop in [2,3,4,5]:

	################## INPUTS ##################

	# relavant paths
	PATH = present_dir+"/"+samples[loop]
	SAVE = PATH+"-rec"
	TEMP = present_dir+"/_temp"

	# projection values
	files = sorted([f for f in os.listdir(os.path.join(present_dir,PATH)) if os.path.isfile(os.path.join(present_dir,PATH,f))])
	number = len(files)
	im = Image.open(os.path.join(PATH,files[0]))
	width, height = im.size
	CoR = width/2

	# reconstruction y-position
	y_start = 0
	y_thick = height
	y_all = np.arange(np.ceil(-height/2),np.ceil(height/2+1),1)
	y_some = np.arange(np.ceil(-y_thick/2),np.ceil(y_thick/2+1),1)
	regionstart = y_all[y_start]
	regionend = y_all[y_start+y_thick]

	# Ellipse values
	laminoangle = 30
	Xc = width/2
	Yc = height/2

	################## COMMANDS ##################

	if run == 1:
		os.system("tofu reco --projections "+PATH+" --output "+os.path.join(SAVE,"sli")+" --overall-angle 360 --axis-angle-x "+str(laminoangle)+" --axis-angle-y 0 --center-position-x "+str(Xc)+" --center-position-z "+str(Yc)+" --region="+str(regionstart)+","+str(regionend)+",1"+ " --output-bytes-per-file 0")

		elapsedtime = str(datetime.now()-starttime)
		print("Finisehd in "+elapsedtime)
		starttime = datetime.now()

