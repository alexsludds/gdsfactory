import gdsfactory as gf

c = gf.components.pad_array180(pad='pad', spacing=[150.0, 150.0], columns=1, rows=3, orientation=180)
c.plot()