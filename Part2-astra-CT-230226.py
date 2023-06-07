from __future__ import division
import numpy as np
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
from imageio import get_writer
import astra
run = 1
present_dir = os.getcwd()


# data parameters
dataset = present_dir+"/dataset-n_grid-01500.txt"
width = 2132 # Number of rows / Horizontal size of detect
height = 1162 # Number of columns / Vertical size of detector [pixels].
proj_n = 1500 # Number of projections
output_dir = present_dir+"/dataset-n_grid-01500-CT-"+str(width)+"x"+str(height)

if run == 1:
    # STEP 1 - Load 3D object, correct orientation
    A = np.loadtxt(dataset, dtype=float, delimiter=",")
    nx2d,ny2d = np.shape(A)
    
    A = np.reshape(A,[int(nx2d),int(ny2d/nx2d),int(nx2d)]) # [x_python, y_python, z_python] corresponds to [x_matlab, z_matlab, y_matlab]
    A = np.rot90(A, k=1, axes=(0,1))
    nx,ny,nz = np.shape(A)

    # STEP 2 - assign 3D object to volume geometry
    # Create astra vol geometry
    vol_geom = astra.creators.create_vol_geom(ny,nz,nx)
    # Assign phantom id as astra volume
    ph_id = astra.data3d.create('-vol', vol_geom, data=A)

    # STEP 3 - create projections
    # Detector and projection information
    angles = np.linspace(0, np.pi, num=proj_n, endpoint=True)
    proj_geom = astra.create_proj_geom('parallel3d', 1, 1, height, width, angles)
    proj_id, proj = astra.creators.create_sino3d_gpu(ph_id, proj_geom, vol_geom)
    proj /= np.max(proj)

    # STEP 4 - Save projections
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    proj = np.round(proj * 65535).astype(np.uint16)
    for i in range(proj_n):
        singleproj = proj[:, i, :]
        with get_writer(os.path.join(output_dir,'proj'+str(i).zfill(len(str(proj_n))+1)+'.tif')) as writer:
            writer.append_data(singleproj, {'compress': 9})
