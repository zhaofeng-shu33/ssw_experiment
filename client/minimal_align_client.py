"""
An example of a "bare-bones" client for performing parallelzed SSW using AWS Lambda.
Upon completion, results should be located in your S3 bucket.
"""

import pathlib
import os

import boto3

from client_config import lambdaName, sqsQueueUrl, s3ResultsBucket
import lambda_client as lc

if os.environ.get('partition'):
    TOTAL_PARTITIONS = int(os.environ.get('partition'))
else:
    TOTAL_PARTITIONS = 1
def createTasks():
    totalPartitions = TOTAL_PARTITIONS
    tasks = set()
    for i in range(1, totalPartitions + 1):
        for j in range(i, totalPartitions + 1):
            tasks.add(lc.Task(
                command=[
                    r"/tmp/ssw_test",
                    r"-pl",
                    r"/var/task/proteinPartitions/partition" + str(i) + ".fasta",
                    r"/var/task/proteinPartitions/partition" + str(j) + ".fasta",
                    r"./BLOSUM62",
                    r"-o 10",
                    r"-e 1"
                ],
                name=str(i) + "-" + str(j),
                executableName="ssw_test",
                lambdaFunctionName=lambdaName
                )
            )
    return tasks

def createJob(concurrencyLimit):
    job = lc.Job(
        tasks=createTasks(),
        concurrencyLimit=concurrencyLimit,
        sqsQueueUrl=sqsQueueUrl,
        s3Bucket=s3ResultsBucket
    )
    return job

def downloadResults(s3Bucket, resultsPath):
    pathlib.Path(resultsPath).mkdir(parents=True, exist_ok=True)
    my_bucket = boto3.resource('s3').Bucket(s3Bucket)

    for object in my_bucket.objects.all():
        my_bucket.download_file(object.key, resultsPath + object.key)

def main():
    concurrencyLimit = 1000
    job = createJob(concurrencyLimit)
    print("Starting tasks")
    job.executeAllTasks()
    print("Done")

main()