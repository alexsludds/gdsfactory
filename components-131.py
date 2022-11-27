import gdsfactory as gf

c = gf.components.pack_doe(doe='mmi1x2', do_permutations=False)
c.plot()