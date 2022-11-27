import gdsfactory as gf

c = gf.components.cutback_component(cols=4, rows=5, port1='o1', port2='o2', mirror=False, cross_section='strip')
c.plot()