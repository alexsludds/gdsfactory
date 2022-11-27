import gdsfactory as gf

components = [gf.components.triangle(x=i) for i in range(1, 10)]
c = gf.grid_with_text(
    components,
    shape=(1, len(components)),
    rotation=0,
    h_mirror=False,
    v_mirror=True,
    spacing=(100, 100),
    text_offsets=((0, 100), (0, -100)),
    text_anchors=("nc", "sc"),
)
c.plot()