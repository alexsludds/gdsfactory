import gdsfactory as gf

c = gf.Component("get_routes_bend180")
pad_array = gf.components.pad_array(orientation=270)
c1 = c << pad_array
c2 = c << pad_array
c2.rotate(90)
c2.movex(1000)
c2.ymax = -200

routes_bend180 = gf.routing.get_routes_bend180(
    ports=c2.get_ports_list(), radius=75 / 2,
)
c.add(routes_bend180.references)

routes = gf.routing.get_bundle(
    c1.get_ports_list(), routes_bend180.ports,
)
for route in routes:
    c.add(route.references)
c.show(show_ports=True)
c.plot()