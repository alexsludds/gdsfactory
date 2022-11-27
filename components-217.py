import gdsfactory as gf

c = gf.components.via_stack_slot_m1_m2(size=[11.0, 11.0], layers=['M1', 'M2'], layer_offsets=[0, 1.0], enclosure=1.0, ysize=0.5, yspacing=2.0)
c.plot()