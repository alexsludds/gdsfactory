import gdsfactory as gf

c = gf.components.edge_coupler_array(n=5, pitch=127.0, x_reflection=False, text_offset=[10, 20])
c.plot()