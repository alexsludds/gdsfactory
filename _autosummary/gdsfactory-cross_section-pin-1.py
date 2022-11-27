import gdsfactory as gf

xs = gf.cross_section.pin(width=0.5, via_stack_gap=1, via_stack_width=1)
p = gf.path.arc(radius=10, angle=45)
c = p.extrude(xs)
c.plot()