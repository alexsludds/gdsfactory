import gdsfactory as gf

c = gf.components.taper_strip_to_ridge(length=10.0, width1=0.5, width2=0.5, w_slab1=0.15, w_slab2=6.0, layer_wg='WG', layer_slab='SLAB90', cross_section='strip')
c.plot()