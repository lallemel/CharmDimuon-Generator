# generate_data_files_1.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script uses the 100 config files with extension *_neutrinoConfig.json and the script inject_muons.py to generate 100 data files of 10,000 
(anti)neutrino events. Each file has the extension *_li.h5, where * is the random seed. Some files with the extension *_lw.lic are also generated.
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/LeptonInjector/'

for i in range(1, 101):
    random_seed = 110000 + i
    config_file_path = 'config_files/' + str(random_seed) + '_neutrinoConfig.json'
    h5_file_path = 'data_files/' + str(random_seed) + '_li.h5'

    gen_cmd = ['python3', 'basic_files/inject_muons.py', '-c', config_file_path]
    subprocess.run(gen_cmd, cwd=cwd)
    
    # there is a bug to be fixed in the generated file
    fix_cmd = ['python3', 'basic_files/fix_primary.py', '-f', h5_file_path]
    subprocess.run(fix_cmd, cwd=cwd)
