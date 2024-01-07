import json
import math

import boto3
from time import gmtime, strftime

# get database table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DB_NAME)

# get current time instance
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# get second lambda function
secondLambda = boto3.client('lambda')

# get EC2 instances
region = REGION
ec2 = boto3.client('ec2',region_name=region)

def lambda_handler(event, context):

    if int(event['amount']) > 1000000:
        instance = [EC2_INSTANCE_ID]
        
        ec2.stop_instances(InstanceIds=instance)
        
        return {
        'statusCode': 200,
        'body': json.dumps("Stopped ec2 instance" +str(instance))
        }
    
    # extract data from event
    amount = float(event['amount'])
    interest = float(event['interest']) * 0.01
    maturity = int(event['maturity'])
    
    # do calculations
    total_amount = amount * (1 + interest)**maturity
    monthly_amount = total_amount / maturity
    
    # call second lambda function if caculation method is 'detailed'
    if event['operation'] == 'detailed':
        message = {"amount": str(amount), "total_amount": str(total_amount), "monthly_amount" : str(monthly_amount), "maturity" : str(maturity)}
        
        responseFromSecondLambda = secondLambda.invoke(
            FunctionName=ARN_OF_SECOND_LAMBDA,
            InvocationType='RequestResponse',
            Payload=json.dumps(message),
        )
            
        secondLambdaResponse = json.load(responseFromSecondLambda['Payload'])
        
        return secondLambdaResponse

    # write results to DynamoDB table
    response = table.put_item(
        Item={
            'ID':now,
            'Total Amount': str(total_amount),
            'Maturity': str(maturity),
            'Interest': str(interest),
            'Monthly Payment': str(monthly_amount)
            })

    return {
    'statusCode': 200,
    'body': json.dumps('Your Monthly Payment is : ' + str( round(monthly_amount, 2)))
    }