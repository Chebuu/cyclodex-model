from os.path import normpath

from nglview import show_mdtraj
from mdtraj import Topology, Trajectory

from simtk import unit
from simtk.openmm.app import PDBFile

def render_traj(topology, positions):
    traj = Trajectory(
        positions/unit.nanometers, 
        Topology.from_openmm(topology))
    return (nglview.show_mdtraj(traj)
        .add_ball_and_stick('all')
        .center_view(zoom=True))

def save_model_pdb(topology, positions, filename):
    with open(filename, 'w') as pdbfile:
        if save: PDBFile.writeFile(topology, positions, pdbfile)

def save_frames_pdb(pdb, start=0, stop=0, step=1, where='./', name='frame-%s'):
    isfname = isinstance(pdbfile, PDBFile) 
    nformat = name if not isfname else pdb.split('.pdb') + name
    nformat = (nformat if '%' in nformat else nformat + '%s') + '.pdb'
    pdbfile = pdb if isfname else PDBFile(pdbfile)
    topology = pdbfile.getTopology()
    stop = stop if stop else pdbfile.getNumFrames()
    for idx in range(start, stop, step):
        positions = pdbfile.getPositions(frame=stop)
        filepath = path.normpath(where + '/' + nformat % step)
        PDBFile.writeFile(topology, positions, filepath, True)
        
def echo_context_energy(context):
    message = '\n\tkinetic: %s\n\tpotential: %s '
    state = context.getState(getEnergy=True)
    ekinetic = state.getKineticEnergy()
    epotential = state.getPotentialEnergy()
    return message % (ekinetic, epotential)
