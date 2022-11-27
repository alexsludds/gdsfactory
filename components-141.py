import gdsfactory as gf

c = gf.components.pads_shorted(columns=8, pad_spacing=150.0, layer_metal='M3', metal_width=10)
c.plot()