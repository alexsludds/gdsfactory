import gdsfactory as gf

c = gf.components.grating_coupler_tree(n=4, straight_spacing=4.0, with_loopback=False, bend='bend_euler', fanout_length=0.0, layer_label='TEXT')
c.plot()