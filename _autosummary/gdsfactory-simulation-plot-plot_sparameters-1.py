import gdsfactory as gf
import gdsfactory.simulation as sim

sp = sim.get_sparameters_data_lumerical(component=gf.components.mmi1x2)
sim.plot.plot_sparameters(sp, logscale=True)