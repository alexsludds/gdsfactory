import gdsfactory as gf

components = [gf.components.triangle(x=i) for i in range(1, 10)]
c = gf.pack(
    components,
    spacing=20.0,
    max_size=(100, 100),
    text=gf.partial(gf.components.text, justify="center"),
    text_prefix="R",
    name_prefix="demo",
    text_anchors=["nc"],
    text_offsets=[(-10, 0)],
    v_mirror=True,
)
c[0].plot()