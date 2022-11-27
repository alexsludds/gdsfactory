import gdsfactory as gf

c = gf.Component("get_routes_straight")
pad_array = gf.components.pad_array()
c1 = c << pad_array
c2 = c << pad_array
c2.ymax = -200

routes = gf.routing.get_routes_straight(ports=c1.get_ports_list(), length=200)
c.add(routes.references)
c.plot()