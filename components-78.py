import gdsfactory as gf

c = gf.components.edge_coupler_silicon(length=100, width1=0.5, width2=0.2, with_bbox=True, with_two_ports=False, cross_section='strip')
c.plot()