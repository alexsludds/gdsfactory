import gdsfactory as gf

c = gf.components.straight_heater_metal()
cc = gf.routing.add_electrical_pads_top(component=c, spacing=(-150, 30))
cc.plot()