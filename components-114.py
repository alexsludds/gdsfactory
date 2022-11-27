import gdsfactory as gf

c = gf.components.mmi_90degree_hybrid(width=0.5, width_taper=1.7, length_taper=40.0, length_mmi=175.0, width_mmi=10.0, gap_mmi=0.8, with_bbox=True, cross_section='strip')
c.plot()