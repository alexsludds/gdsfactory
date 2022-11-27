import gdsfactory as gf
c = gf.components.nxn(west=2, east=2)

cc = gf.routing.fanout2x2(component=c, port_spacing=20)
cc.plot()