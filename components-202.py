import gdsfactory as gf

c = gf.components.text_lines(text=['Chip', '01'], size=0.4, layer='WG')
c.plot()