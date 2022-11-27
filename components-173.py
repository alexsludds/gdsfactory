import gdsfactory as gf

c = gf.components.straight_heater_metal(length=320.0, length_undercut_spacing=6.0, length_undercut=30.0, length_straight_input=15.0, heater_width=2.5, cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section_heater_undercut='strip_heater_metal_undercut', with_undercut=False, port_orientation1=180, port_orientation2=0, heater_taper_length=5.0)
c.plot()