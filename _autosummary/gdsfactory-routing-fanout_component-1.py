import gdsfactory as gf
c = gf.components.mmi2x2()

cc = gf.routing.fanout_component(
    component=c, port_names=tuple(c.get_ports_dict(orientation=0).keys())
)
cc.plot()