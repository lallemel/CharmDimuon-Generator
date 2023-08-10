# Step 4: PROPOSAL

## Propagation of the Daughter Particles in Water

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

This step consists in running PROPOSAL to propagate the daughter particles (two muons and two hadrons) of the previously obtained I3MCTree through water and the detector volume.

## Terminal Set-Up

From this step onward, we will need a dedicated IceCube/P-ONE IceTray environment (which is not free/open-source anymore).

```bash
# get the IceTray environment
cd /data/p-one/gaertner/pone_offline/

# get the particle propagator script
cd /data/p-one/<USERNAME>/dimuon_generator/
mkdir PROPOSAL
cd PROPOSAL
cp /data/p-one/llallement/dimuon_generator/PROPOSAL/instructions_4/*
```

The original script I worked with can be found here if needed:
```bash
cp /data/icecube/ssarkar/dimuon_generator/pone_sim/run_proposal.py
```

## PROPOSAL

```bash
# run the particle propagator
python3 run_proposal.py -i <WEIGHTED I3 FILE PATH> -o <OUTPUT I3 FILE PATH> -r <RANDOM SEED>
```

The run_proposal.py script will run PROPOSAL to propagate all the daughter particles in water. At the end of the run, each input file will produce a new output file with a 'new' I3MCTree containing the list of propagated particles. The muons now have definite lengths and there might be additional daughter particles. The old I3MCTree is now renamed 'I3MCTree_preMuon_Prop' in the latest output file.

I have a script to run the run_proposal.py script over all the .i3 files:
```bash
python3 generate_data_files_4.py
```
