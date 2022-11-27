import gdsfactory as gf

c = gf.components.cutback_component_mirror(cols=4, rows=5, port1='o1', port2='o2', mirror=True, cross_section='strip')
c.plot()