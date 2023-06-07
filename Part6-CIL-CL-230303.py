import numpy as np
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
import subprocess
import time
from datetime import datetime
from PIL import Image
from imageio import get_writer
from cil.io import TIFFStackReader, TIFFWriter
from cil.utilities.display import show2D, show_geometry
from cil.framework import DataContainer, AcquisitionData, AcquisitionGeometry
from cil.processors import CentreOfRotationCorrector, Padder, Slicer
from cil.optimisation.algorithms import Algorithm, CGLS, FISTA
from cil.optimisation.functions import IndicatorBox, L1Norm, LeastSquares, TotalVariation, ZeroFunction
from cil.plugins.ccpi_regularisation.functions import FGP_TV
from cil.plugins.astra import FBP, ProjectionOperator
run = 1
present_dir = os.getcwd()

samples = "n_grid-500-CL-736x622"

for loop in [100]:

	print("Part 1 - Set variables")
	print(">>> check record folder if it exists")
	if not os.path.isdir(os.path.join(present_dir,"_log")):
		os.mkdir(os.path.join(present_dir,"_log"))
	lognum = len([f for f in os.listdir(os.path.join(present_dir,"_log")) if os.path.isfile(os.path.join(present_dir,"_log",f))])

	print(">>> pre set information")
	PATH = present_dir+"/"+samples

	fileanmes = sorted([f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH,f))])
	number = len(fileanmes)
	im = Image.open(os.path.join(PATH,fileanmes[0]))
	width, height = im.size
	tiltdeg = 30 # laminography angle in degrees
	tiltrad = -((tiltdeg*np.pi)/180) # laminography angle in radians
	SSD = -55 # source to sample distance (SSD) in m
	SDD = 0.04 # sample to detector distance (SDD) in m
	COR = 0

	print("Part 2 - create acquisition geometry")
	ag = AcquisitionGeometry.create_Parallel3D( \
		detector_position=[0.0, SDD, 0.0], \
		rotation_axis_position=[COR, 0.0, 0.0], \
		rotation_axis_direction=[0.0, -np.sin(tiltrad), np.cos(tiltrad)]) \
	     .set_angles(angles=np.linspace(0,360,number), angle_unit='degree') \
	     .set_panel(num_pixels=[width, height],  origin='top-left')
	print(">>> read data as acquisition data")
	data = TIFFStackReader(file_name=PATH).read_as_AcquisitionData(ag)
	print(data)
	print(">>> reorder data to astra")
	data.reorder(order='astra')
	print(">>> acquisition geometry:")
	ag = data.geometry
	print(ag)
	print(">>> image geometry:")
	ig = ag.get_ImageGeometry()
	print(ig)


	if run == 1:
		print("Part 3 - iterative reconstruction")
		print(">>> setup projection operator")
		A = ProjectionOperator(ig, ag)
		b = data
		x0 = ig.allocate()
		iterations = loop
		howmanyruns = loop
		# FISTA
		if run == 1:
			print(">>> setup fista")
			# F = LeastSquares(A, data, c=0.5)
			F = LeastSquares(A, data)
			if run == 0:
				print(">>> fista alone")
				# G = ZeroFunction()
				G = IndicatorBox(lower=0.0)
			if run == 0:
				print(">>> fista with l1 regularizer")
				alpha = 100
				G = alpha*L1Norm()
			if run == 0:
				print(">>> fista with tv regularizer")
				alpha = 0.02
				G = alpha*TotalVariation()
			if run == 1:
				print(">>> GPU accelerated tv regularization")
				alpha = 1
				G = alpha*FGP_TV(max_iteration=iterations, device='gpu')
		print(">>> initializing")
		myFISTA = FISTA(initial=x0, f=F, g=G, max_iteration=iterations)
		myFISTA.run(howmanyruns,verbose=1)
		print(">>> starting")
		recon = myFISTA.solution
		method = "FISTA GPU accelerated TV regularization, alpha = "+str(alpha)+", iterations = "+str(iterations)+", runs = "+str(howmanyruns)
		output_dir = os.path.join(present_dir,"test-"+str(lognum).zfill(4)+"-runs-"+str(howmanyruns)+"-it-"+str(iterations)+"-alpha-"+str(alpha))

	if run == 0:
		print("Part 3 - iterative reconstruction")
		print(">>> FBP gpu accelerated")
		recon = FBP(ig,ag,device='gpu')(data)
		method = "astra FBP gpu"
		output_dir = os.path.join(present_dir,"test-"+str(lognum).zfill(4))

	if run == 1:
		print("Part 4 - Save images")
		print(">>> load recon as array")
		sli = DataContainer.as_array(recon)
		print(">>> saving")
		if not os.path.isdir(output_dir):
			os.mkdir(output_dir)
		slisize = sli.shape
		print(sli.shape)
		for i in range(slisize[1]):
			singlesli = sli[:,i,:]
			with get_writer(os.path.join(output_dir, 'sli-'+str(i).zfill(4)+'.tif')) as writer:
				writer.append_data(singlesli, {'compress': 9})

		print("Part 5 - make log file")
		loglines = ["dataset = "+PATH\
			   ,"number = "+str(number)+" projections"\
			   ,"width = "+str(width)+" pixels"\
			   ,"height = "+str(height)+" pixels"\
			   ,"tiltdeg = "+str(tiltdeg)+" deg"\
			   ,"tiltrad = "+str(tiltrad)+" rad"\
			   ,"SSD = "+str(SSD)+" m"\
			   ,"SDD = "+str(SDD)+" m"\
			   ,"COR = "+str(COR)\
			   ,"method = "+method]
		with open(os.path.join(present_dir,"_log","test-"+str(lognum).zfill(4)+".txt"), 'w') as f:
			f.write('\n'.join(loglines))




