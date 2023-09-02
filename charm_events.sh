# !/bin/bash
# charm_events.sh

cd /data/p-one/llallement/dimuon_generator/PYTHIA/job_submission/

export DIMUON_REPO=/data2/icecube/ssarkar/test_singularity/gitrepo
export PYTHONPATH=$DIMUON_REPO/modules:$PYTHONPATH
export LHAPDF_DATA_PATH=$DIMUON_REPO/data/pdfsets

make dire08

input_file=$1
output_file=$2

./dire08 nu_ccdis.cmnd "$input_file" "$output_file"
