import gdsfactory as gf

c = gf.components.add_fiducials_offsets(fiducial='cross', offsets=[[0, 100], [0, -100]])
c.plot()