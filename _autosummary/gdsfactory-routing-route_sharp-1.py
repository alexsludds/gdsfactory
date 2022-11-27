import gdsfactory as gf

c = gf.Component("pads")
c1 = c << gf.components.pad(port_orientation=None)
c2 = c << gf.components.pad(port_orientation=None)

c2.movex(400)
c2.movey(-200)

route = c << gf.routing.route_sharp(c1.ports["e4"], c2.ports["e1"], path_type="L")
c.plot()