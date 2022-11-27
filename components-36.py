import gdsfactory as gf

c = gf.components.compensation_path(direction='top', cross_section='strip')
c.plot()