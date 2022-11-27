import gdsfactory as gf

c = gf.components.pad(size=[100.0, 100.0], layer='M3', port_inclusion=0)
c.plot()