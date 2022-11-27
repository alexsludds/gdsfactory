import gdsfactory as gf

c = gf.components.optimal_90deg(width=100, num_pts=15, length_adjust=1, layer=[1, 0])
c.plot()