# Step 2: PYTHIA

## Primary Interaction and Hadronization

Author: Louise Lallement Arnaud  
Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr  
Working with: Sourav Sarkar, Juan Pablo Yáñez

The target nucleons are sampled based on their composition in water. Using PYTHIA and DIRE framework and the previously generated neutrino energies, a million muon neutrino CC DIS interactions with the target nucleons are simulated to produce outgoing muons and charm quarks, which then undergo the hadronization process.

## Terminal Set-Up

```bash
# copy the relevant files
cd /data/p-one/<USERNAME>/dimuon_generator/
mkdir PYTHIA
cd PYTHIA/
cp -r /data/p-one/llallement/dimuon_generator/PYTHIA/instructions_2/* .
```

The original files I worked with can be found here if needed:
```bash
cp $DIMUON_REPO/scripts/charm_config.py .
cp $DIMUON_REPO/scripts/dire08.cc .
cp $DIMUON_REPO/scripts/Makefile* .
cp $DIMUON_REPO/scripts/nu_ccdis.cmnd .
```

We are still working in the same Singularity container.

```bash
# set up the proper terminal variables
export DIMUON_REPO=/data2/icecube/ssarkar/test_singularity/gitrepo
export PYTHONPATH=$DIMUON_REPO/modules:$PYTHONPATH
export LHAPDF_DATA_PATH=$DIMUON_REPO/data/pdfsets
```

## Interaction Target Sampler

The target for the incoming neutrino is water (10 Hydrogen atoms and 8 Oxygen atoms per water molecule). The target sampler (file charm_config.py that was copied) generates sampled config files with extension *_charmConfig.txt. We use the config and .h5 files generated in the first step with the LeptonInjector.

```bash
# produce sampled configuration text output
python3 charm_config.py -f <H5 FILE PATH> -c <CONFIG FILE PATH>
```

The resulting file contains 4 columns of data: event ID, incoming neutrino PDG code, neutrino energy in GeV and target code (1 for proton, 2 for neutron).

I wrote a script to run this command for all 100 config and .h5 files from the first step. It was copied earlier. Again, check the datapath!

```bash
# generate config files
python3 generate_config_files_2.py
```

## PYTHIA

PYTHIA+DIRE software (with C++ code dire08) will produce an output text file containing the following information:
- each row starting with 'E' marks the start of a new event list;
- in the event 'E' row, the other information are: neutrino PDG code, event ID, energy, target type;
- in the following 'P' rows, daughter particles information from the PYHTIA+DIRE simulated events are stored;
- each 'P' row has the following information: particle index, PDG code, energy, theta, phi (zenith and azimuth equivalent angles in an LHC-like z-axis coordinate system).

```bash
# compile the C++ code
make dire08

# execute the compiled code
./dire08 nu_ccdis.cmnd <CONFIG FILE PATH> <OUTPUT FILE NAME>
```

The config file here is a sampled config file with extension *_charmConfig.txt generated before and the output file name must contain a *.txt extension.

## Job Submission

The code above takes ~1h to run for each chunk of 10k events. It becomes necessary to submit these as CPU jobs on HTCondor. I ran 100 jobs with the same submission file charm_events.sub. It excecutes the charm_events.sh bash script. There is a datapath to be updated in the bash script. The submission file must specify a Singularity image, check that path! All the other paths should start from the directory where the submission and bash files are located.

It is probably not mandatory, but I created a special directory with all the necessary files and sub-directories to run the job. Along the submission and executable files, I have the nu_ccdis.cmnd and dire08.cc files (+ Makefile, Makefile.inc, but not sure if these are needed) and five directories for input config files (with the 100 _charmConfig.txt files) and output data files as well as .log, .out and .err files.

```bash
# submit the job
condor_submit charm_events.sub
```

The files I generated can be found here:
```bash
cp -r /data/p-one/llallement/dimuon_generator/PYTHIA/results_2/ .
```

The executable file should compile dire08, but it does not always. It would be safer to compile it yourself before submitting the job.

## Data Analysis

A Jupyter notebook can be found among the copied files. It contains a few plots of some properties of the charm quarks/hadrons: hadrons distribution, inelasticity distribution, mean inelasticity and mean opening angles. These plots have been validated in team meetings and can somewhat be used as references when generating your own data. Their validation was based on people's prior knowledge and on two papers: https://arxiv.org/pdf/hep-ex/0102049.pdf (Fig. 7), https://arxiv.org/pdf/1808.07629.pdf (Fig. 8).
