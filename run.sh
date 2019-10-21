#!/bin/bash
set -e -x
mkdir -p originalData
if [ ! -f originalData/uniprot_humanProteinList.fasta ]; then
  cd originalData
  wget "https://www.uniprot.org/uniprot/?query=reviewed:yes%20AND%20proteome:up000005640&format=fasta&force=true&compress=yes" -O uniprot_humanProteinList.fasta.gz
  gunzip uniprot_humanProteinList.fasta.gz
fi
cd ../lambdaPackage
python partitionProteins.py 
