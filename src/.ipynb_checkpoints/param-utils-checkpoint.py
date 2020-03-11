# https://github.com/choderalab/openmoltools/blob/718f50277e5656cdd96babcec9abc9c4e90b6f64/openmoltools/amber.py
# https://github.com/choderalab/openmoltools/blob/f2ffa08bf026f5b9e0e1354f51e78b33c8290e83/openmoltools/utils.py

from os.path import normpath

def parameterize_smiles(smiles_strings, base_molecule_name, output_dir='./'):
    """Generate an MDTraj object from a smiles string.
    Parameters
    ----------
    smiles_strings : list(str)
        Smiles strings to create molecules for
    base_molecule_name : str, optional, default='lig'
        Base name of molecule to use inside parameter files.
    Returns
    -------
    traj : mdtraj.Trajectory
        MDTraj object for molecule
    ffxml : StringIO
        StringIO representation of ffxml file.
    Notes
    -----
    ffxml can be directly input to OpenMM e.g.
    `forcefield = app.ForceField(ffxml)`
    """
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
    except ImportError:
        raise(ImportError("Must install rdkit to use smiles conversion."))

    amber = import_("openmoltools.amber")        

    gaff_mol2_filenames = []
    frcmod_filenames = []
    trajectories = []
    for k, smiles_string in enumerate(smiles_strings):
        molecule_name = "%s-%d" % (base_molecule_name, k)
        m = Chem.MolFromSmiles(smiles_string)
        m = Chem.AddHs(m)
        AllChem.EmbedMolecule(m)
        AllChem.UFFOptimizeMolecule(m)
        
        mdl_filename = tempfile.mktemp(suffix=".mdl")
        Chem.MolToMolFile(m, mdl_filename)
        
        frcmod_filename = normpath(
            output_dir + '/' + molecule_name + '.gaff.mol2')
        gaff_mol2_filename = normpath(
            output_dir + '/' + molecule_name + '.frcmod')
        
        gaff_mol2_filename, frcmod_filename = amber.run_antechamber(
            input_format='mdl',
            molecule_name=molecule_name, 
            ligand_filename=mdl_filename, 
            frcmod_filename=frcmod_filename)
        
        traj = md.load(gaff_mol2_filename)
        for atom in traj.top.atoms:
            atom.residue.name = molecule_name

        gaff_mol2_filenames.append(gaff_mol2_filename)
        frcmod_filenames.append(frcmod_filename)
        trajectories.append(traj)

    ffxml = create_ffxml_file(
        gaff_mol2_filenames=gaff_mol2_filenames, 
        frcmod_filenames=frcmod_filenames, 
        override_mol2_residue_name=molecule_name)

    return trajectories, ffxml