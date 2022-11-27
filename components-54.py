import gdsfactory as gf

c = gf.components.crossing_etched(width=0.5, r1=3.0, r2=1.1, w=1.2, L=3.4, layer_wg='WG', layer_slab='SLAB150')
c.plot()