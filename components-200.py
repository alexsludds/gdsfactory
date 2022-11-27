import gdsfactory as gf

c = gf.components.text(text='abcd', size=10.0, position=[0, 0], justify='left', layer='WG')
c.plot()