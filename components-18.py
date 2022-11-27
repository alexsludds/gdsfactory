import gdsfactory as gf

c = gf.components.bend_circular180(angle=180, npoints=720, with_bbox=True, cross_section='strip')
c.plot()