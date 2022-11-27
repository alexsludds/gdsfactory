import gdsfactory.simulation.simphony as gs
import gdsfactory.simulation.simphony.components as gc

c = gc.ring_single()
gs.plot_circuit(c)