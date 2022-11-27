import gdsfactory as gf

c = gf.components.ramp(length=10.0, width1=5.0, width2=8.0, layer='WG')
c.plot()