import gdsfactory as gf

c = gf.components.cavity(coupler='coupler', length=0.1, gap=0.2)
c.plot()