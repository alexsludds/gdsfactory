import gdsfactory as gf

c = gf.components.coh_tx_single_pol(balanced_phase_shifters=False, mzm_y_spacing=50.0, phase_shifter='straight_pin', phase_shifter_length=100.0, mzm_ps_spacing=40.0, splitter='mmi1x2', mzm_length=200.0, with_pads=True, xspacing=40.0, pad_array='pad_array', cross_section='strip')
c.plot()