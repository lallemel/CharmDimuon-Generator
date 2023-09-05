# generate_i3_track_files.py

# Author: Louise Lallement Arnaud
# Contact: lallemen@ualberta.ca or louise.lallement@etu.univ-grenoble-alpes.fr

'''
This script runs the run_doubletrack.py script over all the propagated .i3 files. The output files have the extension *_trackOutput.i3.gz and can be use to calculate the event rates of dimuon events in the detector.
'''



import subprocess

cwd = '/scratch/lallemen/PROPOSAL/doubletrack_run/'

for i in range(1, 101):
    random_seed = 110000 + i
    input_file = '/scratch/lallemen/PROPOSAL/i3_propagated_files/' + str(random_seed) + '_propagatedOutput.i3.gz'
    output_file = '/scratch/lallemen/PROPOSAL/i3_track_files/' + str(random_seed) + '_trackOutput.i3.gz'
    
    gen_cmd = ['python3', 'run_doubletrack.py', '-i', input_file, '-o', output_file]
    subprocess.run(gen_cmd, cwd=cwd)
