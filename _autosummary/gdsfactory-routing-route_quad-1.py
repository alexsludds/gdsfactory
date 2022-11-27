import gdsfactory as gf

c = gf.Component()
pad1 = c << gf.components.pad(size=(50, 50))
pad2 = c << gf.components.pad(size=(10, 10))
pad2.movex(100)
pad2.movey(50)
route_gnd = c << gf.routing.route_quad(
    pad1.ports["e2"],
    pad2.ports["e4"],
    width1=None,
    width2=None,
)
c.show()
c.plot()