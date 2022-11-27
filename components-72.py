import gdsfactory as gf

c = gf.components.die(size=[10000.0, 10000.0], street_width=100.0, street_length=1000.0, die_name='chip99', text_size=100.0, text_location='SW', layer='FLOORPLAN', bbox_layer='FLOORPLAN', draw_corners=True, draw_dicing_lane=True)
c.plot()