import gdsfactory as gf

c = gf.components.grating_coupler_rectangular(n_periods=20, period=0.75, fill_factor=0.5, width_grating=11.0, length_taper=150.0, polarization='te', wavelength=1.55, layer_slab='SLAB150', fiber_marker_layer='TE', slab_xmin=-1.0, slab_offset=1.0, cross_section='strip')
c.plot()