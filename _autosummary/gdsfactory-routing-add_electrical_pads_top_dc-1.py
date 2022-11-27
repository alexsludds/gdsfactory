import gdsfactory as gf
c = gf.components.straight_heater_metal(length=100)
c = gf.routing.add_electrical_pads_top_dc(c, width=10)
c.plot()