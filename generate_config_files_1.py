# generate_config_files_1.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script updates the original LeptonInjector config file LI_config.json to create 100 different config files (different random seeds), each set up to generate 10k events. Half of the files are to generate neutrino events (seed [110001, 110050]), and the other half are for antineutrino events (seed [110051, 110100]). The generated files have the extension *_neutrinoConfig.json, where * is the seed.
'''



import json
import copy

datapath = '/data/p-one/llallement/dimuon_generator/LeptonInjector/'
input_file = datapath + 'basic_files/LI_config.json'
particle_type = ['MuMinus', 'MuPlus']

with open(input_file, 'r') as file:
    original_data = json.load(file)

for i, particle in enumerate(particle_type):
    data = copy.deepcopy(original_data)
    data['LeptonInjector']['finalType_1'] = particle

    for j in range(1, 51):
        random_seed = 110000 + i * 50 + j
        data_copy = copy.deepcopy(data)
        data_copy['LeptonInjector']['random_seed'] = random_seed
        
        output_file = str(random_seed) + '_neutrinoConfig.json'
        
        with open(datapath + 'config_files/' + output_file, 'w') as file:
            json.dump(data_copy, file, indent=4)
