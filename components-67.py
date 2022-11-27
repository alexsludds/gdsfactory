import gdsfactory as gf

c = gf.components.delay_snake(length=1600.0, L0=5.0, n=2, bend='bend_euler', cross_section='strip')
c.plot()