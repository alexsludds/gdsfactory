import gdsfactory as gf

c = gf.Component("demo_route_sbend")
mmi1 = c << gf.components.mmi1x2()
mmi2 = c << gf.components.mmi1x2()
mmi2.movex(50)
mmi2.movey(5)
route = gf.routing.get_route_sbend(mmi1.ports['o2'], mmi2.ports['o1'])
c.add(route.references)
c.show()
c.plot()