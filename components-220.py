import gdsfactory as gf

c = gf.components.wafer(reticle='die', cols=[2, 6, 6, 8, 8, 6, 6, 2])
c.plot()