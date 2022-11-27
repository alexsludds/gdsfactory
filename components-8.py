import gdsfactory as gf

c = gf.components.add_grating_couplers_with_loopback_fiber_single(layer_label=[200, 0], gc_port_name='o1', with_loopback=True, loopback_xspacing=5.0, rotation=90)
c.plot()