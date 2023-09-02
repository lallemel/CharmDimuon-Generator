# Step 4: PROPOSAL

## Daughter Particle Propagation

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

The primary and secondary muons, as well as the two hadrons generated along the way, are propagated through water and the detector volume.

## Terminal Set-Up

From this step onward, we will need a dedicated IceCube/P-ONE IceTray environment (which is not free/open-source anymore).

```bash
# get the IceTray environment
cd /data/p-one/gaertner/pone_offline/
source env-shell_RHEL.sh

# copy the relevant files
cd /data/p-one/<USERNAME>/dimuon_generator/
mkdir PROPOSAL
cd PROPOSAL
cp -r /data/p-one/llallement/dimuon_generator/PROPOSAL/instructions_4/*
```

The original particle propagator script I worked with can be found here if needed:
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
python3 generate_i3_propagated_files_4.py
```

## Moving to Cedar for Double-Track Run

The Illume cluster experienced some technical issues as I worked on this step, so I had to move to the Cedar cluster. The following instructions are to be run on Cedar. However, I copied all the files to my Illume space and they can probably be run on there with a few adjustments.

We are still working in the same Singularity container. The singularity image must be imported to Cedar if working on there; I put it among the files to be copied.

```bash
# copy the relevant files to your Cedar scratch space
cp -r /projects/def-nahee/lallemen/PROPOSAL/ /scratch/<CEDAR USERNAME>/

# load the Singularity environment
cd PROPOSAL
singularity shell -B /scratch:/scratch -B /cvmfs:/cvmfs nudimuon-generator_v1.0.sif

# load the standard IceTray framework
cd /opt/icetray-public/build/
./env-shell.sh

# run the run_doubletrack.py file
python3 run_doubletrack.py -i <PROPOSAL OUTPUT I3 FILE PATH> -o <OUTPUT I3 FILE PATH>
```

As always, I have a script to run this last command over all the files:
```bash
python3 generate_i3_track_files.py
```

The generated files can then be transferred to Illume to continue working on there. Run this command in Illume:
```bash
scp -r <CEDAR USERNAME>@cedar.computecanada.ca:<PATH TO I3 TRACK FILES DIRECTORY> /data/p-one/<USERNAME>/dimuon_generator/PROPOSAL/
``` 

## Event Rates

Back in Illume, set up the usual Singularity and IceCube environments. A directory called event_rate was previously copied. It contains a Jupyter notebook that can be used as an example of how to use the .i3 files to calculate event rates.






