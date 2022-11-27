import gdsfactory as gf

c = gf.components.add_grating_couplers_with_loopback_fiber_array(grating_separation=127.0, gc_port_name='o1', gc_rotation=-90, straight_separation=5.0, layer_label=[200, 0], with_loopback=False, nlabels_loopback=2, loopback_yspacing=4.0)
c.plot()