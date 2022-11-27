import gdsfactory as gf

xs = gf.cross_section.cross_section(width=0.5, offset=0, layer='WG')
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()