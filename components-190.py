import gdsfactory as gf

c = gf.components.taper_from_csv(cross_section='strip')
c.plot()