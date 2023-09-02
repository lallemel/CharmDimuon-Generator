# generate_h5_files_3.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script runs the charm muon generator over the 100 PYTHIA output files (from Step 2). The generated files have the extension *_dimuonOutput.h5, where * is the original random seed. Each generated file contains an event particle list located in the 'EventParticleList' object within the file.
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/NuDimuonGenerator/NuDimuon-Generator/modules/'

for i in range(1, 101):
    random_seed = 110000 + i
    input_file_path = '/data/p-one/llallement/dimuon_generator/PYTHIA/txt_files/' + str(random_seed) + '_charmOutput.txt'
    output_file_path = '/data/p-one/llallement/dimuon_generator/NuDimuonGenerator/h5_files/' + str(random_seed) + '_dimuonOutput.h5'
    
    gen_cmd = ['python3', 'get_charm_muons.py', '-i', input_file_path, '-o', output_file_path, '-m', 'water', '-s', str(random_seed)]
    subprocess.run(gen_cmd, cwd=cwd)
