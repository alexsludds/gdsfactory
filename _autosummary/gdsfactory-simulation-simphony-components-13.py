import gdsfactory.simulation.simphony as gs
import gdsfactory.simulation.simphony.components as gc

c = gc.ring_double()
gs.plot_circuit(c)