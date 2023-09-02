# generate_i3_weighted_files_3.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script takes the .i3 files with extension *_output.i3.gz and uses a bunch of other files to update them with event weights, through the script compute_weights.py. The generated files have the extension *_weightedOutput.i3.gz.
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/NuDimuonGenerator/NuDimuon-Generator/scripts/weight_generation_run/'
datapath = '/data/p-one/llallement/dimuon_generator/'

for i in range(1, 101):
    random_seed = 110000 + i
    i3_non_weighted_file = datapath + 'NuDimuonGenerator/i3_files/' + str(random_seed) + '_output.i3.gz'
    h5_lepton_injector_file = datapath + 'LeptonInjector/h5_files/' + str(random_seed) + '_li.h5'
    h5_charm_muon_file = datapath + 'NuDimuonGenerator/h5_files/' + str(random_seed) + '_dimuonOutput.h5'
    config_lepton_injector_file = datapath + 'LeptonInjector/config_files/' + str(random_seed) + '_neutrinoConfig.json'
    output_file = datapath + 'NuDimuonGenerator/i3_weighted_files/' + str(random_seed) + '_weightedOutput.i3.gz'
    
    gen_cmd = ['python3', 'compute_weights.py', '-i', i3_non_weighted_file, '-l', h5_lepton_injector_file, '-c', h5_charm_muon_file, '-f', config_lepton_injector_file, '-o', output_file]
    subprocess.run(gen_cmd, cwd=cwd)