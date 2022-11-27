import gdsfactory as gf

c = gf.components.bend_port(port_name='e1', port_name2='e2', cross_section='metal3_with_bend', angle=180)
c.plot()