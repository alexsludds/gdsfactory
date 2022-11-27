import gdsfactory as gf

c = gf.components.via2(size=[0.7, 0.7], spacing=[2.0, 2.0], enclosure=1.0, layer='VIA2', bbox_offset=0)
c.plot()