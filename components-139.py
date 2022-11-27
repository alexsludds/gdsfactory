import gdsfactory as gf

c = gf.components.pad_gsg_open(size=[22, 7], layer_metal='M3', metal_spacing=5.0, short=False, pad_spacing=150)
c.plot()