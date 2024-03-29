[![Build Status](https://dev.azure.com/zhaofengshu33/ssw_experiment/_apis/build/status/zhaofeng-shu33.ssw_experiment?branchName=master)](https://dev.azure.com/zhaofengshu33/ssw_experiment/_build/latest?definitionId=1&branchName=master)
[![Gitlab](https://gitlab.com/zhaofeng-shu33/ssw_experiment/badges/master/pipeline.svg)](https://gitlab.com/zhaofeng-shu33/ssw_experiment)
[![Build Status](https://travis-ci.com/zhaofeng-shu33/ssw_experiment.svg?branch=master)](https://travis-ci.com/zhaofeng-shu33/ssw_experiment)
[![CircleCI](https://circleci.com/gh/zhaofeng-shu33/ssw_experiment.svg?style=svg)](https://circleci.com/gh/zhaofeng-shu33/ssw_experiment)

# SSW Experiment on DevOps

This experiment uses DevOps agent to run the SSW Experiment, two versions are provided:
* Local running on DevOps agent
* DevOps agent as client to invoke AWS lambda function

The purpose of this repository is to enhance the experiment reproducibility of the SSW Experiment.

See the paper [Leveraging Serverless Computing to Improve Performance for Sequence Comparison](https://github.com/Egria/website/raw/master/Serverless_ParBio_ACM_BCB.pdf) for the detail of original SSW Experiment.

## Limitations
* The client user account and lambda role are created manually.
* Binding to a target aws service endpoint, not configurable.
