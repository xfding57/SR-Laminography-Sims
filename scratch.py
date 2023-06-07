import numpy as np
import os
present_dir = os.getcwd()
PATH = "dataset-n_grid-01500-CT-2132x1162"

files = sorted([f for f in os.listdir(os.path.join(present_dir,PATH)) if os.path.isfile(os.path.join(present_dir,PATH,f))])
number = len(files)

for i in np.arange(0,3002,2):
	# print(files[i])
	print("proj"+str(i).zfill(5)+".tif")
