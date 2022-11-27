import gdsfactory as gf

components = [gf.components.triangle(x=i) for i in range(1, 10)]
c = gf.grid(
    components,
    shape=(1, len(components)),
    rotation=0,
    h_mirror=False,
    v_mirror=True,
    spacing=(100, 100),
)
c.plot()