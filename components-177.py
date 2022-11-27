import gdsfactory as gf

c = gf.components.straight_pin(length=500.0, via_stack_width=10.0, via_stack_spacing=2)
c.plot()