import gdsfactory as gf

xs = gf.cross_section.strip_heater_metal_undercut(width=0.5, heater_width=2, trench_width=4, trench_gap=4)
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()