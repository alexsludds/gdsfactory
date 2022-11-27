import gdsfactory as gf

c = gf.components.taper_adiabatic(width1=0.5, width2=5.0, length=0, alpha=1, wavelength=1.55, npoints=200, cross_section='strip')
c.plot()