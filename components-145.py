import gdsfactory as gf

c = gf.components.rectangle(size=[4.0, 2.0], layer='WG', centered=False, port_type='placement', port_orientations=[180, 90, 0, -90])
c.plot()