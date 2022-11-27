from gdsfactory.simulation.simphony.components.mzi import mzi
import gdsfactory.simulation.simphony as gs

c = mzi()
gs.plot_circuit_montecarlo(c)