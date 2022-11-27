import gdsfactory as gf

c = gf.components.ring_single(width=0.5, gap=0.2, length_x=4, radius=5, length_y=2)
c.plot()