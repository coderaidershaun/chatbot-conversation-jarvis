import boto3

s3 = boto3.resource('s3')
bucket_name = 'chatbot-chatgpt'


# Upload S3 bucket information
def upload_audio(file):
  s3.Bucket(bucket_name).upload_fileobj(Fileobj=file, Key="audio",
                                      ExtraArgs={"ACL": "bucket-owner-full-control"})

