import gdsfactory as gf

c = gf.components.coh_rx_single_pol(bend='bend_euler', cross_section='strip', det_spacing=[60.0, 50.0], with_pads=True, pad_det_spacing=80.0, in_wg_length=20.0)
c.plot()