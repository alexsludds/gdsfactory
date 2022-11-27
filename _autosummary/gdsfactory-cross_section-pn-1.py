import gdsfactory as gf

xs = gf.cross_section.pn(width=0.5, gap_low_doping=0, width_doping=2.)
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()