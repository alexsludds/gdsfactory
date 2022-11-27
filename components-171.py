import gdsfactory as gf

c = gf.components.straight_heater_doped_strip(length=320.0, nsections=3, via_stack_metal_size=[10.0, 10.0], via_stack_size=[10.0, 10.0], with_taper1=True, with_taper2=True, heater_width=2.0, heater_gap=0.8, via_stack_gap=0.0, width=0.5, xoffset_tip1=0.2, xoffset_tip2=0.4)
c.plot()