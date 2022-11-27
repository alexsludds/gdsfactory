import gdsfactory as gf

c = gf.components.taper_sc_nc(length=20.0, width1=0.5, width2=0.15, w_slab1=0.15, w_slab2=1.0, layer_wg='WG', layer_slab='WGN', cross_section='strip')
c.plot()