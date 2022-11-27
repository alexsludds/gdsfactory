import gdsfactory as gf

c = gf.components.ring_double()
c = gf.Component()
ref = c << gf.components.ring_double()
r = gf.routing.route_south(ref)
for e in r.references:
    c.add(e)
c.plot()