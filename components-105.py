import gdsfactory as gf

c = gf.components.litho_ruler(height=2, width=0.5, spacing=2.0, scale=[3, 1, 1, 1, 1, 2, 1, 1, 1, 1], num_marks=21, layer='WG')
c.plot()