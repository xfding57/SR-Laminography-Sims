import os
import subprocess
import numpy as np
import shutil
from datetime import datetime
run = 1
starttime = datetime.now()
totaltime = datetime.now()
present_dir = os.getcwd()
def root_path():
	return os.path.abspath(os.sep)


PATH = os.path.join(present_dir,"dataset-n_grid-01000-CT-1424x810-rec-CL-1470x1470")
SAVE = os.path.join(present_dir,"dataset-n_grid-01000-CT-1424x810-rec-CL-1470x1470-v2")
desirednum = 180

# get number of files inside the desired directory
files = sorted([f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH,f))])
filesnum = np.size(files)
reduceby = filesnum/desirednum
# copy files
if run == 1:
	if not os.path.isdir(SAVE):	
		os.mkdir(SAVE)
	for j in np.arange(0,filesnum,reduceby):
		print(files[j])
		shutil.copy(os.path.join(PATH,files[j]), os.path.join(SAVE,files[j]))

