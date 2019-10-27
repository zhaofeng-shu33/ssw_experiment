#!/bin/bash
pip install --user boto3     
cd client
wget https://gitlab.com/zhaofeng-shu33/ssw_experiment/-/jobs/333800685/artifacts/download -O artifacts.zip
unzip artifacts.zip
python verify_result.py
export AWS_DEFAULT_REGION=us-east-2
cat verification.txt