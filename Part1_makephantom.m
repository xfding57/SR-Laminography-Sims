run = 1;
close all
if run == 1
    clear
    clc
end
tStart = cputime;
t1 = cputime;
run = 1;

n_grid = 1500;
im3D = ones(n_grid,n_grid);
% make markings
if run == 1
    for hideloop = 1
        % left side markings
        mksz = floor([0.03, 0.02, 0.01, 0.006, 0.002, 0.001]*n_grid);
        absbottompad = 0.04;
        bottompad = floor([absbottompad, absbottompad*2+0.27, absbottompad*3+0.45, absbottompad*4+0.54, absbottompad*4+0.54, absbottompad*4+0.57]*n_grid);
        absleftpad = 0.04;
        leftpad = floor([absleftpad, absleftpad, absleftpad, absleftpad, absleftpad*2+0.09,absleftpad*2+0.09]*n_grid);
        mkwidth = floor([0.27, 0.18, 0.18, 0.09, 0.09-absleftpad, 0.09-absleftpad]*n_grid);
        for j = 1:6
            for i = 1:2:9
                im3D((n_grid-bottompad(j)-mksz(j)*i):(n_grid-bottompad(j)-mksz(j)*(i-1)),leftpad(j):leftpad(j)+mkwidth(j)) = 0;
            end
        end
        % right side markings
        mksz = floor([0.03, 0.02, 0.01, 0.006, 0.002, 0.001]*n_grid);
        absbottompad = 0.04;
        bottompad = floor([absbottompad, absbottompad+0.33, absbottompad+0.57, absbottompad+0.6050, absbottompad+0.5750, absbottompad+0.5750]*n_grid);
        absrightpad = 0.04;
        rightpad = floor([absrightpad, absrightpad, absrightpad, absrightpad+0.12, absrightpad+0.12, absrightpad+0.15]*n_grid);
        mkwidth = floor([0.2700, 0.1800, 0.0900, 0.0540, 0.0180, 0.0180]*n_grid);
        for j = 1:6
            for i = 1:2:9
                im3D((n_grid-bottompad(j)-mkwidth(j)):(n_grid-bottompad(j)),n_grid-rightpad(j)-mksz(j)*i:n_grid-rightpad(j)-mksz(j)*(i-1)) = 0;
            end
        end
        % center bottom
        mksz = floor([0.0060    0.0050    0.0040    0.0030    0.0020    0.0010]*n_grid);
        absbottompad = 0.3900;
        bottompad = floor([absbottompad, absbottompad-0.01-0.054, absbottompad-0.01*2-0.054*2, absbottompad-0.01*3-0.054*3, absbottompad-0.01*4-0.054*4, absbottompad-0.01*5-0.054*5]*n_grid);
        absleftpad = 0.3700;
        leftpad = floor(absleftpad*n_grid);
        mkwidth = floor(0.0540*n_grid);
        for j = 1:6
            for i = 1:2:9
                im3D(n_grid-bottompad(j):n_grid-bottompad(j)+mkwidth,leftpad+mksz(j)*(i-1):leftpad+mksz(j)*i) = 0;
            end
        end
        mksz = floor([0.0060    0.0050    0.0040    0.0030    0.0020    0.0010]*n_grid);
        absbottompad = 0.3900;
        bottompad = floor([absbottompad, absbottompad-0.01-0.054, absbottompad-0.01*2-0.054*2, absbottompad-0.01*3-0.054*3, absbottompad-0.01*4-0.054*4, absbottompad-0.01*5-0.054*5]*n_grid);
        absleftpad = 0.4600;
        leftpad = floor(absleftpad*n_grid);
        mkwidth = floor(0.0540*n_grid);
        for j = 1:6
            for i = 1:2:7
                im3D(n_grid-bottompad(j)+mksz(j)*(i-1):n_grid-bottompad(j)+mksz(j)*i,leftpad:leftpad+mkwidth) = 0;
            end
        end
        % center middle
        mksz = floor([0.0060    0.0050    0.0040    0.0030    0.0020    0.0010]*n_grid);
        absbottompad = 0.5700;
        bottompad = floor(absbottompad*n_grid);
        absleftpad = 0.3100;
        leftpad = floor([absleftpad, absleftpad+0.0100+0.0540, absleftpad+0.0100*2+0.0540*2, absleftpad+0.0100*3+0.0540*3, absleftpad+0.0100*4+0.0540*4, absleftpad+0.0100*5+0.0540*5]*n_grid);
        mkwidth = floor(0.0540*n_grid);
        for j = 1:6
            for i = 1:2:9
                im3D(n_grid-bottompad+mksz(j)*(i-1):n_grid-bottompad+mksz(j)*i,leftpad(j):leftpad(j)+mkwidth) = 0;
            end
        end
        mksz = floor([0.0060    0.0050    0.0040    0.0030    0.0020    0.0010]*n_grid);
        absbottompad = 0.4900;
        bottompad = floor(absbottompad*n_grid);
        absleftpad = 0.3100;
        leftpad = floor([absleftpad, absleftpad+0.0100+0.0540, absleftpad+0.0100*2+0.0540*2, absleftpad+0.0100*3+0.0540*3, absleftpad+0.0100*4+0.0540*4, absleftpad+0.0100*5+0.0540*5]*n_grid);
        mkwidth = floor(0.0540*n_grid);
        for j = 1:6
            for i = 1:2:9
                im3D(n_grid-bottompad:n_grid-bottompad+mkwidth,leftpad(j)+mksz(j)*(i-1):leftpad(j)+mksz(j)*i) = 0;
            end
        end
        for i = 1:4
            im3D = cat(3,im3D,im3D);
        end
        im3D = cat(3,im3D,ones(n_grid,n_grid,90));
    end
end
% show 3d plot
if run == 0
    imshow3D(im3D)
end
% save data as txt file
if run == 0
    dlmwrite(join(['dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'.txt']), im3D)
end
% save padded data as txt file
if run == 1
    lamino = 30;
    [nx,ny,nz] = size(im3D);
    padvalue = 10;
    padxy = round(sqrt(2*(nx^2)))+padvalue;
    padz = round(sind(lamino)*sqrt(2*(nx^2))+ sind(90-lamino)*nz)+padvalue;
    im3Dr = padarray(im3D,[round((padxy-n_grid)/2) round((padxy-n_grid)/2) round((padz-nz)/2)],0,'both');
    [nxr,nyr,nzr] = size(im3Dr)
    if run == 0
        % imwrite(im3Dr,join(['dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'.tif']))
        dlmwrite(join(['dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'-pad.txt']), im3Dr)
    end
end


if run == 0
    % rotate 3d object
    % laminography angle
    lamino = 30;
    % pad original image depending on laminography angle and original dimensions
    [nx,ny,nz] = size(im3D);
    padvalue = 10;
    padxy = round(sqrt(2*(nx^2)))+padvalue;
    padz = round(sind(lamino)*sqrt(2*(nx^2))+ sind(90-lamino)*nz)+padvalue;
    % rotation step size
    step = 5;
    for j = 0:step:360-step
        disp(j)
        im3Dr = padarray(im3D,[round((padxy-n_grid)/2) round((padxy-n_grid)/2) round((padz-nz)/2)],0,'both');
        % rotate 3d object
        im3Dr = imrotate3(im3Dr,j,[0 0 1],'linear','crop');
        im3Dr = imrotate3(im3Dr,lamino,[-1 0 0],'linear','crop');
        [nxr,nyr,nzr] = size(im3Dr);
        
        % write data to disk
        disp(join(["saving projection ",num2str(j)]))
        if j == 0
            % makefolder for output
            mkdir(join(['/staff/dingx/Desktop/Local_data/dingx/220302-prj35G12338-Hydrogel/rec/XFDing/3-Software/4-CIL/230226/dataset-n_grid-',pad(num2str(n_grid),5,'left','0')]))
            % save 0 and 360 degrees
            dlmwrite(join(['/staff/dingx/Desktop/Local_data/dingx/220302-prj35G12338-Hydrogel/rec/XFDing/3-Software/4-CIL/230226/dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'/proj00000.txt']), im3Dr)
            dlmwrite(join(['/staff/dingx/Desktop/Local_data/dingx/220302-prj35G12338-Hydrogel/rec/XFDing/3-Software/4-CIL/230226/dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'/proj00360.txt']), im3Dr)
        else
            % save other projection steps
            dlmwrite(join(['/staff/dingx/Desktop/Local_data/dingx/220302-prj35G12338-Hydrogel/rec/XFDing/3-Software/4-CIL/230226/dataset-n_grid-',pad(num2str(n_grid),5,'left','0'),'/proj',pad(num2str(j),5,'left','0'),'.txt']), im3Dr)
        end
        
        disp([j,nxr,nyr,nzr])
        t2 = cputime;
        disp(join(["dataset finished in ",num2str(t2-t1)," seconds"]))
        t1 = cputime;
    end
end

tEnd = cputime-tStart;
disp(join(['Finished in ',num2str(tEnd),' seconds']))

