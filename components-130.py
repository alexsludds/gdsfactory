import gdsfactory as gf

c = gf.components.optimal_step(start_width=10, end_width=22, num_pts=50, width_tol=0.001, anticrowding_factor=1.2, symmetric=False, layer=[1, 0])
c.plot()