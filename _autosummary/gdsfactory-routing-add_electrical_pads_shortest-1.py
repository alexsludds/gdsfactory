import gdsfactory as gf
c = gf.components.straight_heater_metal(length=100)
c = gf.routing.add_electrical_pads_shortest(c, port_orientation=270)
c.plot()