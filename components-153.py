import gdsfactory as gf

c = gf.components.ring_single_array(spacing=5.0, cross_section='strip')
c.plot()