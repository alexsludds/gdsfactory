import gdsfactory as gf

c = gf.components.text_freetype(text='abcd', size=10, justify='left', layer='WG', font='DEPLOF')
c.plot()