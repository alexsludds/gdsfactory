import gdsfactory as gf

c = gf.components.fiducial_squares(layers=[[1, 0]], size=[5, 5], offset=0.14)
c.plot()