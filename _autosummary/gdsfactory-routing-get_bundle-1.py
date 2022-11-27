import gdsfactory as gf

@gf.cell
def test_north_to_south():
    dy = 200.0
    xs1 = [-500, -300, -100, -90, -80, -55, -35, 200, 210, 240, 500, 650]

    pitch = 10.0
    N = len(xs1)
    xs2 = [-20 + i * pitch for i in range(N // 2)]
    xs2 += [400 + i * pitch for i in range(N // 2)]

    a1 = 90
    a2 = a1 + 180

    ports1 = [gf.Port(f"top_{i}", center=(xs1[i], +0), width=0.5, orientation=a1, layer=(1,0)) for i in range(N)]
    ports2 = [gf.Port(f"bot_{i}", center=(xs2[i], dy), width=0.5, orientation=a2, layer=(1,0)) for i in range(N)]

    c = gf.Component()
    routes = gf.routing.get_bundle(ports1, ports2)
    for route in routes:
        c.add(route.references)

    return c


gf.config.set_plot_options(show_subports=False)
c = test_north_to_south()
c.plot()