import gdsfactory as gf

c = gf.components.taper(length=10.0, width1=0.5, with_bbox=True, with_two_ports=True, cross_section='strip')
c.plot()