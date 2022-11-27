import gdsfactory as gf

c = gf.components.resistance_sheet(width=10, layers=['SLAB90', 'NPP'], layer_offsets=[0, 0.2], pad_pitch=100.0, port_orientation1=180, port_orientation2=0)
c.plot()