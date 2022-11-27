import gdsfactory as gf

c = gf.components.resistance_meander(pad_size=[50.0, 50.0], num_squares=1000, width=1.0, res_layer='M3', pad_layer='M3', gnd_layer='M3')
c.plot()