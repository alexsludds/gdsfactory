import gdsfactory as gf

c = gf.components.taper_strip_to_ridge_trenches(length=10.0, width=0.5, slab_offset=3.0, trench_width=2.0, trench_layer='SLAB90', layer_wg='WG', trench_offset=0.1)
c.plot()