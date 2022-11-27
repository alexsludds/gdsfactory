import gdsfactory as gf

c = gf.components.bezier(width=0.5, control_points=[[0.0, 0.0], [5.0, 0.0], [5.0, 2.0], [10.0, 2.0]], npoints=201, with_manhattan_facing_angles=True, cross_section='strip', with_bbox=True)
c.plot()