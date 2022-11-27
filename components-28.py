import gdsfactory as gf

c = gf.components.cdc(length=30.0, gap=0.5, period=0.22, dc=0.5, dx=10.0, dy=5.0, width_top=2.0, width_bot=0.75, fins=False, fin_size=[0.2, 0.05])
c.plot()