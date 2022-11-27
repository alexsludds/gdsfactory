import gdsfactory as gf

c = gf.components.coupler90bend(radius=10.0, gap=0.2, cross_section_inner='strip', cross_section_outer='strip')
c.plot()