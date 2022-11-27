import gdsfactory as gf

c = gf.components.pad_array90(pad='pad', spacing=[150.0, 150.0], columns=6, rows=1, orientation=90)
c.plot()