import gdsfactory as gf

c = gf.components.ring_double_heater(gap=0.2, radius=10.0, length_x=0.01, length_y=0.01, cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section='strip', port_orientation=90, via_stack_offset=[0, 0])
c.plot()