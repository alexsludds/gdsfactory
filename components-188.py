import gdsfactory as gf

c = gf.components.taper_cross_section_parabolic(length=10, npoints=101, linear=False, width_type='parabolic')
c.plot()