# Step 1: LeptonInjector

## Generation of Muon (Anti)Neutrino CC DIS Events

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

This step consists in running the LeptonInjector to generate 1,000,000 charged current deep inelastic scattering (CC DIS) muon (anti)neutrino events.

## Singularity Container

This work should be implemented within the Singularity container:

```bash
# go to personal data directory
cd /data/p-one/<USERNAME>

# pull the container image file (only once)
singularity pull --arch amd64 library://ssarkarbht/simgen/nudimuon-generator:v1.0

# launch a bash shell with data directories bound in the container
singularity shell -B /data:/data -B /data2:/data2 -B /cvmfs:/cvmfs nudimuon-generator_v1.0.sif
```

## LeptonInjector Event Generator

```bash
# set up the LeptonInjector software
cd /data/p-one/<USERNAME>
mkdir dimuon_generator
cd dimuon_generator
mkdir LeptonInjector
cd LeptonInjector
cp /data/p-one/llallement/dimuon_generator/LeptonInjector/instructions_1/*
```

The original files I worked with can be found here if needed:
```bash
cp /data2/icecube/ssarkar/dimuon_scripts/scripts/
```

This will copy some files, among which:
- LI_config.json, a config file;
- inject_muons.py, a script to generate neutrino CC DIS events;
- fix_primary.py, a script to fix a bug.

The parameters in the config file should match these:

```java
"random_seed" : 1101011, // does not matter
"xs_folder" : "/cvmfs/icecube.opensciencegrid.org/data/neutrino-generator/cross_section_data/csms_differential_v1.0/",
"earth_model" : "/data2/icecube/ssarkar/dimuon_scripts/data/EarthModels/",
"event_number" : 10000,
"ranged_mode" : true,
"finalType_1" : "MuMinus", // for neutrinos, change to "MuPlus" for antineutrinos
"finalType_2" : "Hadrons",
"MinEnergy" : 50.0, // [GeV]
"MaxEnergy" : 1000000.0, // [GeV]
"gamma"     : 1.5,
"MinZenith" : 80.0, // [deg]
"MaxZenith" : 180.0, // [deg]
"MinAzimuth" : 0.0, // [deg]
"MaxAzimuth" : 360.0, // [deg]
"injRadius" : 400.0, // [m]
"endLength" : 800.0, // [m]
"out_folder" : "./data_files/", // should be checked and changed accordingly
"out_filename" : "li.h5",
"lw_filename" : "lw.lic"
```

```bash
# run the LeptonInjector
python3 inject_muons.py -c <CONFIG FILE PATH>

# fix a bug in the LeptonInjector
python3 fix_primary.py -f <H5 FILE NAME>
```

This will generate two files: a .h5 file and a .lic file. The .h5 file contains data for the incoming muon (anti)neutrino, the outgoing (anti)muon and a generic hadron carrying the rest of the energy.

## Config and Data Files Generation

The goal here is to simulate 1,000,000 neutrino CC DIS events: 500k muon neutrino events and 500k muon antineutrino events. I chose to generate chunks of 10k events and hence required 50 different config files with different seeds for each incoming particle type.

Two files were previously copied:
- generate_config_1.py, a script to generate 100 config files with different random seeds ([110001, 110050] for neutrino events and [110051, 110100] for antineutrino events);
- generate_data_files_1.py, a script to run the inject_muons.py and fix_primary.py scripts over the 100 config files.

Check the indicated datapaths carefully! There is also a datapath indicated in the orginal LI_config.json that should be updated accordingly.

```bash
# generate 100 config files
python3 generate_config_files_1.py

# generate the corresponding data files
python3 generate_data_files_1.py
```

The config files have the extension *_neutrinoConfig.json and the data files have the extension *_li.h5, where * is the random seed.

The files I generated can be found here:
```bash
cp /data/p-one/llallement/dimuon_generator/LeptonInjector/results_1/
```
