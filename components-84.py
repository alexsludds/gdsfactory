import gdsfactory as gf

c = gf.components.ge_detector_straight_si_contacts(length=80.0, via_stack_width=10.0, via_stack_spacing=5.0)
c.plot()