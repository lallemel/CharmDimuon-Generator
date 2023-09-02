# Step 3: NuDimuon-Generator & IceTray

## a) Charm Hadron Decay and Interaction, b) Event Weight Calculation

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

a) The charm hadrons are simulated to either decay into a muon or interact into water before decay. The muon energy is sampled using a parametrization technique.

b) Each event is assigned a Monte Carlo event weight in Hz. It represents the probability of the event occurring given the true simulated quantities. The calculation of the weight depends on the chosen flux model, as well as different weight factors arising from each step of the simulation.

## Terminal Set-Up

```bash
# copy the relevant files
cd /data/p-one/<USERNAME>/dimuon_generator
mkdir NuDimuonGenerator
cd NuDimuonGenerator
cp /data/p-one/llallement/dimuon_generator/NuDimuonGenerator/instructions_3/*
```

The original files I worked with can be found here if needed:
```bash
git clone https://github.com/ssarkarbht/NuDimuon-Generator.git
```

We are still working in the same Singularity container.

```bash
# set up environment variables
cd NuDimuon-Generator
source setup.sh
```

## Charm Muon Generator

```bash
# go to the module directory
cd modules

# run the charm muon generator
python3 get_charm_muons.py -i <INPUT TEXT FILE PATH> -o <OUTPUT H5 FILE PATH> -m water -s <RANDOM SEED>
```

The input text file here should be one of the text files generated during Step 2 and containing PYTHIA output. The output file name should include the extension *.h5. I chose to name my output files *_dimuonOutput.h5, where * is the original random seed (carried along from the LeptonInjector). The full absolute path of the input and output files should be provided here.

At the end of the run, a new .h5 file is generated with the final event output particles. The event particle list is in the 'EventParticleList' object within the file. Each individual event is treated as a dataset within this object with the dataset name as the event ID (in string).

I have a script to run this command for all 100 PYTHIA output files:
```bash
python3 generate_h5_files_3.py
```

Be careful! There is a datapath in the get_charm_muons.py script (line 24) that needs to be updated if you did not place the various copied files immediately in the NuDimuonGenerator directory.

## Data Analysis

Among the previously copied files is a Jupyter notebook (data_analysis_3a.ipynb) that plots some basic features of the final generated events. You can have a look at the plots or use the notebook to check your own generated data. None of these plots are of great importance as the events still have not been weighted, but you can have a look all the same.

## IceCube Environment

We are still working in the same Singularity container.

```bash
# load the IceCube environment
cd /opt/icetray-public/build/
./env-shell.sh

# update the charm dimuon generator repository (if needed)
cd NuDimuonGenerator/
git reset --hard origin/main
git pull

# load the repository setup
cd NuDimuon-Generator
source setup.sh
```

## Addition of P-ONE Geometry

We will now take the first .h5 files we produced using the LeptonInjector (which contain geometry information) and the .h5 files that we just generated using the charm muon generator (which contain event kinematics) and merge them into .i3 files.

```bash
# run the script
cd .../NuDimuon-Generator/scripts/event_merger_run/
python3 convert_h5toi3.py -i <LEPTON INJECTOR H5 FILE PATH> -f <CHARM MUON H5 FILE PATH> -o <OUTPUT I3 FILE PATH> -s <RANCOM SEED>
```

The output file name should have the extension *.i3.gz. The random seed should be the one used in the LeptonInjector file.

I have a script to do that over all the files:
```bash
python3 generate_i3_files_3.py
```

## Event Weight Computation

The weight computed here is called 'OneWeight'. It is independent of the neutrino flux. For more details about it, please see Sourav Sarkar's PhD thesis: https://github.com/ssarkarbht/PhDThesis.

```bash
# compute event weights
cd .../NuDimuon-Generator/scripts/weight_generation_run/
python3 compute_weights.py -i <INPUT I3 FILE PATH> -l <LEPTON INJECTOR H5 FILE PATH> -c <CHARM MUON H5 FILE PATH> -f <LEPTON INJECTOR CONFIG FILE PATH> -o <OUTPUT I3 FILE PATH>
```

The config file here is the very first config file that was generated, with extension *.json. The output file should have extension *.i3.gz.

I have a script to do that over all the files:
```bash
python3 generate_i3_weighted_files_3.py
```

The files I generated can be found here:
```bash
cp /data/p-one/llallement/dimuon_generator/NuDimuonGenerator/results_3/
```

## A Word on .i3 Files

To view the content of an .i3 file, you can run:
```bash
dataio-shovel <I3 FILE NAME>
```

An .i3 file is composed of several frames, labelled with letters. In these .i3 files, the only types of frame we have are information frames (I) and DAQ frames (Q). The I frames hold basic information about the run. The Q frames hold all the event properties we are interested in. One can use the arrow keys to navigate the file, the enter key to access a frame or object and the 'Q' key to exit it.

The final 'weighted' files contain four objects per Q frame:
- I3MCTree contains information about the event kinematics: particle ID, type, position, direction, time, energy and length (which is a NaN as the particles have not been propagated yet);
- I3MCWeightDict contains a lot of information on the event and, most importantly, the OneWeight;
- CharmWeightDict contains some information on the charm quark and hadron;
- I3EventHeader just contains information on the run (not important as this is a simulation).

In order to process .i3 data files, a pipeline needs to be created. A Jupyter notebook has been copied (data_analysis_3b.ipynb) which shows an example of a pipeline that extracts some values and put them into numpy arrays. These properties can then be plotted accordingly. The few plots that can be found in the notebook have been validated by Sourav and can be used as references.
