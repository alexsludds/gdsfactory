import gdsfactory as gf

c = gf.components.grating_coupler_rectangular_arbitrary_slab(gaps=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], widths=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], width_grating=11.0, length_taper=150.0, polarization='te', wavelength=1.55, layer_slab='SLAB150', slab_offset=2.0, fiber_marker_layer='TE', cross_section='strip')
c.plot()