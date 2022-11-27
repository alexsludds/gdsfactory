import gdsfactory as gf

c = gf.components.via_stack(size=[11.0, 11.0], layers=['M1', 'M2', 'M3'])
c.plot()