import gdsfactory as gf

p = gf.path.euler(radius=10, angle=45, p=1, use_eff=True, npoints=720)
p.plot()