import gdsfactory as gf

c = gf.components.add_grating_couplers(layer_label=[200, 0], gc_port_name='o1')
c.plot()