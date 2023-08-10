# Step 3: NuDimuon-Generator

## Addition of a OneWeight to the Events

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

This step consists in getting the previously generated files into the IceCube software IceTray in order to add a weight to each event.

## Terminal Set-Up

```bash
# copy the relevant files
cd /data/p-one/<USERNAME>/dimuon_generator
mkdir NuDimuonGenerator
cd NuDimuonGenerator
cp /data/p-one/llallement/dimuon_generator/NuDimuonGenerator/instructions_2/*
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
python3 get_charm_muons.py -i <INPUT TEXT FILE PATH> -o <OUTPUT H5 FILE NAME> -m water -s <RANDOM SEED>
```

The input text file here should be one of the text files generated during Step 2 and containing PYTHIA output. The output file name should include the extension *.h5. I chose to name my output files *_dimuonOutput.h5, where * is the original random seed (carried along from the LeptonInjector). The full absolute path of the input and output files should be provided here.

At the end of the run, a new .h5 file is generated with the final event output particles. The event particle list is in the 'EventParticleList' object within the file. Each individual event is treated as a dataset within this object with the dataset name as the event ID (in string).

I have a script to run this command for all 100 PYTHIA output files. I store all the final output files into a data_files directory.

```bash
# generate data files
python3 generate_data_files_3.py
```

Be careful! There is a datapath in the get_charm_muons.py script (line 24) that needs to be updated if you did not place the various copied files immediately in the NuDimuon-Generator directory.

The files I generated can be found here:
```bash
cp /data/p-one/llallement/dimuon_generator/NuDimuon-Generator/results_3/
```

## Data Analysis

Among the previously copied files is a Jupyter notebook that plots some basic features of the final generated events. You can have a look at the plots or use the notebook to check your own generated data. None of these plots are of great importance as the events still have not been weighted, but you can have a look all the same.
