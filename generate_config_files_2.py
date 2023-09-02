# generate_config_files_2.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script samples a target nucleus (proton or neutron) for each neutrino event generated in Step 1 using the script charm_config.py. The generated files have the extension *_charmConfig.txt (as decided in the charm_config.py script), where * is the original random seed. Each generated text file contains 10,000 events with neutrino energy and sampled target (1 for proton, 2 for neutron).
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/PYTHIA/'
datapath = '/data/p-one/llallement/dimuon_generator/LeptonInjector/'

for i in range(1, 101):
        random_seed = 110000 + i
        config_file_path = datapath + 'config_files/' + str(random_seed) + '_neutrinoConfig.json'
        h5_file_path = datapath + 'data_files/' + str(random_seed) + '_li.h5'
        
        gen_cmd = ['python3', 'basic_files/charm_config.py', '-f', h5_file_path, '-c', config_file_path]
        subprocess.run(gen_cmd, cwd=cwd)
