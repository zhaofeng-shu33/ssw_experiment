from filecmp import dircmp
import boto3
import pathlib

from client_config import s3ResultsBucket, sqsQueueUrl

def downloadResults(s3Bucket, resultsPath):
    pathlib.Path(resultsPath).mkdir(parents=True, exist_ok=True)
    my_bucket = boto3.resource('s3').Bucket(s3Bucket)

    for object in my_bucket.objects.all():
        my_bucket.download_file(object.key, resultsPath + 'alignmnet' + object.key)

def areFoldersDifferent(dir1, dir2):
    dcmp = dircmp(dir1, dir2)
    differences = len(dcmp.diff_files) + len(dcmp.left_only) + len(dcmp.right_only)
    return differences > 0

def verifyResults(basisResultsPath, trialResultsPath, metricsPath):
    with open(metricsPath + "verification.txt", "w") as output_f:
        if areFoldersDifferent(basisResultsPath, trialResultsPath):
            output_f.write("Basis results at [" + basisResultsPath + "] were DIFFERENT (INCORRECT) from trial results in [" + trialResultsPath + "]\n")
        else:
            output_f.write("Basis results at [" + basisResultsPath + "] were IDENTICAL (CORRECT) to trial results in [" + trialResultsPath + "]\n")

def cleanup(s3Bucket, queueUrl):
    my_bucket = boto3.resource('s3').Bucket(s3Bucket)
    s3Client = boto3.client("s3")
    for object in my_bucket.objects.all():
        s3Client.delete_object(
            Bucket=s3Bucket,
            Key=object.key
        )
    sqsClient = boto3.client("sqs")
    sqsClient.purge_queue(
        QueueUrl=queueUrl
    )

if __name__ == '__main__':
    trialResultsDir = "./results/"
    basisResultsDir = "./lambdaPackage/results/"
    downloadResults(s3ResultsBucket, trialResultsDir)
    verifyResults(basisResultsDir, trialResultsDir, './')
    # cleanup(s3ResultsBucket, sqsQueueUrl)