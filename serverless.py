import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        filename = str(file_obj["s3"]["object"]["key"])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket=bucketname, Key=filename) #Replace your bucket name with yours
        file_content = fileObj["Body"].read().decode("utf-8")
        print(file_content)
    return "Thanks"