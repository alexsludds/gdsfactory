import gdsfactory.simulation.simphony as gs
import gdsfactory.simulation.simphony.components as gc

c = gc.gc1550te()
gs.plot_model(c)