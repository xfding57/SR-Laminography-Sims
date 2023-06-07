from __future__ import division
import numpy as np
import os
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
from imageio import get_writer
from skimage import io
import astra
import argparse
run = 1
present_dir = os.getcwd()

if run == 1:
	parser = argparse.ArgumentParser(description="you know what to do")
	parser.add_argument("-PATH", type=str, default="", help="")
	parser.add_argument("-SAVE", type=str, default="", help="")
	parser.add_argument("-filename", type=str, default="", help="")
	parser.add_argument("-width", type=int, default=2000, help="")
	parser.add_argument("-height", type=int, default=2000, help="")
	args, unparsed = parser.parse_known_args()
	PATH = args.PATH
	SAVE = args.SAVE
	filename = args.filename
	width = args.width
	height = args.height

if run == 1:
	print("STEP 1 - Load 3D object, correct orientation")
	print("reading "+PATH)
	im = io.imread(PATH)
	A = np.array(im)
	A = np.rot90(A, k=1, axes=(2,0))
	A = np.rot90(A, k=1, axes=(1,0))
	nx,ny,nz = np.shape(A)
	print(np.shape(A))

	print("STEP 2 - assign 3D object to volume geometry")
	print("Create astra vol geometry")
	vol_geom = astra.creators.create_vol_geom(ny, nz, nx)
	print("Assign phantom id as astra volume")
	ph_id = astra.data3d.create('-vol', vol_geom, data=A)

	print("STEP3 - create projections")
	proj_n = 1
	angles = np.linspace(0, np.pi, num=proj_n, endpoint=False)
	proj_geom = astra.create_proj_geom('parallel3d', 1, 1, height, width, angles)
	proj_id, proj = astra.creators.create_sino3d_gpu(ph_id, proj_geom, vol_geom)
	proj /= np.max(proj)

	print("STEP 4 - Save projections")
	if not os.path.isdir(SAVE):
		os.mkdir(SAVE)
	proj = np.round(proj * 65535).astype(np.uint16)
	for i in range(proj_n):
		singleproj = proj[:, i, :]
		with get_writer(os.path.join(SAVE,filename)) as writer:
			writer.append_data(singleproj, {'compress': 9})

