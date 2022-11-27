import gdsfactory.simulation.simphony as gs
import gdsfactory.simulation.simphony.components as gc

m = gc.coupler_ring()
gs.plot_model(m)