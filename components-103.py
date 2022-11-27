import gdsfactory as gf

c = gf.components.hline(length=10.0, width=0.5, layer='WG', port_type='optical')
c.plot()