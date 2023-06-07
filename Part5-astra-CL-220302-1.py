import numpy as np
import os
run = 1
present_dir = os.getcwd()

# data parameters
PATH = "dataset-n_grid-01500-CT2132x1162-rec-CLv2"
width = 736 # Number of rows / Vertical size of detector [pixels].
height = 736 # Number of columnes / Horizontal size of detector [pixels].
SAVE = PATH+"-"+str(width)
number = sorted([f for f in os.listdir(os.path.join(present_dir,PATH)) if os.path.isfile(os.path.join(present_dir,PATH,f))])
print(number)

if run == 1:
	# for loop in range(len(number)):
	for loop in [339]:
		filename = number[loop]
		if not os.path.isfile(os.path.join(SAVE,filename)):
			os.system("python3 Part5-astra-CL-220302-2.py -PATH "+os.path.join(PATH,number[loop])+" -SAVE "+SAVE+" -filename "+filename+" -width "+str(width)+" -height "+str(height))
