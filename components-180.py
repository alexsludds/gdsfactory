import gdsfactory as gf

c = gf.components.straight_rib(length=10.0, npoints=2, with_bbox=True)
c.plot()