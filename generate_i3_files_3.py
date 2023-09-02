# generate_i3_files_3.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script takes the .h5 files produced using the LeptonInjector (which contain geometry information) and the .h5 files generated using the charm muon generator (which contain event kinematics) and merge them into .i3 files using the script convert_h5toi3.py. The output files have the extension *_output.i3.gz, where * is the original random seed.
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/NuDimuonGenerator/NuDimuon-Generator/scripts/event_merger_run/'
datapath = '/data/p-one/llallement/dimuon_generator/'

for i in range(1, 101):
    random_seed = 110000 + i
    lepton_injector_file = datapath + 'LeptonInjector/h5_files/' + str(random_seed) + '_li.h5'
    charm_muon_file = datapath + 'NuDimuonGenerator/h5_files/' + str(random_seed) + '_dimuonOutput.h5'
    output_file = datapath + 'NuDimuonGenerator/i3_files/' + str(random_seed) + '_output.i3.gz'
    
    gen_cmd = ['python3', 'convert_h5toi3.py', '-i', lepton_injector_file, '-f', charm_muon_file, '-o', output_file, '-s', str(random_seed)]
    subprocess.run(gen_cmd, cwd=cwd)