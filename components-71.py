import gdsfactory as gf

c = gf.components.dicing_lane(size=[50, 300], layer_dicing='DICING')
c.plot()