# generate_i3_propagated_files_4.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script runs the run_proposal.py script over all i3 weighted files to propagate all the daughter particles in water using PROPOSAL. At the end of the run, each input file will produce a new output file with a 'new' I3MCTree containing the list of propagated particles. The output files have the extension *_propagatedOutput.i3.gz.
'''



import subprocess

cwd = '/data/p-one/llallement/dimuon_generator/PROPOSAL/'
datapath = '/data/p-one/llallement/dimuon_generator/'

for i in range(1, 101):
    random_seed = 110000 + i
    input_file = datapath + 'NuDimuonGenerator/i3_weighted_files/' + str(random_seed) + '_weightedOutput.i3.gz'
    output_file = datapath + 'PROPOSAL/i3_propagated_files/' + str(random_seed) + '_propagatedOutput.i3.gz'
    
    gen_cmd = ['python3', 'run_proposal.py', '-i', input_file, '-o', output_file, '-s', str(random_seed)]
    subprocess.run(gen_cmd, cwd=cwd)