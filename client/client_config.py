lambdaName = r"arn:aws:lambda:us-east-2:369401945610:function:ssw" #The ARN of the AWS Lambda function
sqsQueueUrl = r"https://sqs.us-east-2.amazonaws.com/369401945610/ssw" #The URL of the AWS SQS Queue
s3ResultsBucket = r"ssw-azure-pipelines" #The bucket name of the AWS S3 Bucket

if os.environ.get('partition'):
    TOTAL_PARTITIONS = int(os.environ.get('partition'))
else:
    TOTAL_PARTITIONS = 1
