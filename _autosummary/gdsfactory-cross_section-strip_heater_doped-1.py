import gdsfactory as gf

xs = gf.cross_section.strip_heater_doped(width=0.5, heater_width=2, heater_gap=0.5)
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()