import gdsfactory as gf

p = gf.path.euler(radius=10)
c = p.extrude(layer=(1, 0), width=0.5)
c.plot()