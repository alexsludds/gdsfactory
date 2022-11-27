import gdsfactory as gf

c = gf.components.pack_doe_grid(doe='mmi1x2', do_permutations=False, with_text=False)
c.plot()