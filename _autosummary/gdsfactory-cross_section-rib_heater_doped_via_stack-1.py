import gdsfactory as gf

xs = gf.cross_section.rib_heater_doped_via_stack(width=0.5, heater_width=2, heater_gap=0.5, layer_heater='NPP')
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()