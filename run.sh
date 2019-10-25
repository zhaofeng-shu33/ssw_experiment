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
if [ "$#" -ne 0 ]; then
  zip -r upload.zip *
else
  python run_local.py
  cat log.txt
fi

