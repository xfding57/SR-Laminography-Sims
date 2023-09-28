# SR-Lamino-Sims
Simulations for computed laminography

## Part 1 - Make phantom for laminography
Using Part1_makephantom.m in MATLAB, make an object resembling a resolution phantom. The structure of the phantom doesn't necessarily have to resemble any real object. Define the padding, laminography angle, and the rotation steps. The padding helps determine the field of view (FOV). If there is no padding or if the padding is too small, the edges of the phantom may rotate out of the FOV. 

320x320 pixel FOV: <br />
![Forward Project](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/gridwidth-0002-0320-proj.gif)

550x550 pixel FOV: <br />
![Forward Project](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/gridwidth-0002-0550-proj.gif)

1000x1000 pixel FOV: <br />
![Forward Project](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/gridwidth-0002-1000-proj.gif)

For each angular step, a .txt file containing the phantom will be created. This will be read in Part 2.

## Part 2 - Forward project
Using Part2-astra-CT-230226.py. Use ASTRA toolbox (https://github.com/astra-toolbox/astra-toolbox) to forward project each .txt file from Part 1 to create a laminography dataset.

![Forward Project](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/n_grid-500-CL-736x622.gif)


## Part 3 - Laminography Reconstruction
Using Part7-tofu-CL-220303.py. Peform laminography reconstruction using tofu from ufo-kit (https://github.com/ufo-kit/tofu). This is limited to filtered back projection (FBP).

![tofu reconstruction result](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/sli-000-0289.png)

Using Part6-CIL-CL-230303.py. Perform laminography reconstruction using Core Imaging Library (https://github.com/TomographicImaging/CIL). Can use FBP and also a variety of interative reconstruction methods.

![CIL reconstruction result](https://github.com/xfding57/SR-Lamino-Sims/blob/main/media/test-0014-runs-200-it-200-alpha-2.png)


## Part 1 ALT - Make phantom for CT 

- Make phantom in MATLAB in CT orientation
- Use imagej to reorient the faux phantom at the desired laminography angle and angular steps
- Forward project using ASTRA toolbox
- Reconstrct using tofu or CIL