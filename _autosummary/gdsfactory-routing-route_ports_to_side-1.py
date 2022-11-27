import gdsfactory as gf

c = gf.Component('sample_route_sides')
dummy = gf.components.nxn(north=2, south=2, west=2, east=2)
sides = ["north", "south", "east", "west"]
d = 100
positions = [(0, 0), (d, 0), (d, d), (0, d)]

for pos, side in zip(positions, sides):
    dummy_ref = dummy.ref(position=pos)
    c.add(dummy_ref)
    routes, ports = gf.routing.route_ports_to_side(dummy_ref, side, layer=(1, 0))
    for route in routes:
        c.add(route.references)
    for i, p in enumerate(ports):
        c.add_port(name=f"{side[0]}{i}", port=p)

c.plot()