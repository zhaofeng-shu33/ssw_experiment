#!/bin/bash
set -e -x
mkdir -p originalData
cd originalData
if [ ! -f uniprot_humanProteinList.fasta ]; then
  wget "https://www.uniprot.org/uniprot/?query=reviewed:yes%20AND%20proteome:up000005640&format=fasta&force=true&compress=yes" -O uniprot_humanProteinList.fasta.gz
  gunzip uniprot_humanProteinList.fasta.gz
fi
cd ../lambdaPackage
mkdir -p proteinPartitions
python partitionProteins.py 
cd ../ssw
make
cp ssw_test ../lambdaPackage/
cd ../lambdaPackage
# ./run.sh with at least one parameter
if [ "$#" -ne 0 ]; then
  zip -r upload.zip * # travis
else
  if [ -z "$AZURE" ]; then # local
    mkdir -p results
    python alignProteins.py 2>&1 | tee align.log
  else # azure pipelines
    export AWS_DEFAULT_REGION=us-east-2
    cd ../client
    pip install boto3
    python minimal_align_client.py
  fi
fi

