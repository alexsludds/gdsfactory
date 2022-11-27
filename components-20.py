import gdsfactory as gf

c = gf.components.bend_euler(angle=90.0, p=0.5, with_arc_floorplan=True, npoints=720, direction='ccw', with_bbox=True, cross_section='strip')
c.plot()