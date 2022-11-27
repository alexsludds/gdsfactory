import gdsfactory as gf

c = gf.components.grating_coupler_dual_pol(period_x=0.58, period_y=0.58, x_span=11, y_span=11, length_taper=150.0, width_taper=10.0, polarization='dual', wavelength=1.55, base_layer='WG', cross_section='strip', fiber_marker_layer='TE')
c.plot()