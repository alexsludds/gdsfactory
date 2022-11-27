import gdsfactory as gf

c = gf.components.text_rectangular_multi_layer(text='abcd', layers=['WG', 'M1', 'M2', 'M3'])
c.plot()