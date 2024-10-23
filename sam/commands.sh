# Create a S3 Bucket
aws s3 mb s3://sam-bucket-demo-for-aws-dev-associate

# Build CloudFormation template
aws cloudformation package --template-file template.yaml --s3-bucket sam-bucket-demo-for-aws-dev-associate --output-template-file build/generated.yaml

# Deploy the template
aws cloudformation deploy --template-file build/generated.yaml --stack-name hello-from-sam --capabilities CAPABILITY_IAM
