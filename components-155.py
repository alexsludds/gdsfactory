import gdsfactory as gf

c = gf.components.ring_single_heater(gap=0.2, radius=10.0, length_x=4.0, length_y=0.6, cross_section_waveguide_heater='strip_heater_metal', cross_section='strip', port_orientation=90, via_stack_offset=[0, 0])
c.plot()