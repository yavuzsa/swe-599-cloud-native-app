# SWE 599 Project: Cloud Native Application

## To Open The UI
Simply open ` index.html ` file with your browser or run it using you favorite _live server_ extension.  
I have put JavaScript codes and CSS styles inside this single html file. No other dependency to worry about (of course it would not be connected to any backend if you don't have AWS services to back it up).  

I have omitted the ` API_URL ` in the request. It is replaced with the API Gateway URL to access our deployed API. 

## Example Requests

```json 

{
  "amount": 20000,          // Number (decimal)
  "interest": 2.8,          // Number (decimal)
  "maturity": 24,           // Number (integer)
  "operation": "simple"     // String
}

```

```json

{
  "amount": 340000,
  "interest": 3.4,
  "maturity": 50,
  "operation": "detailed"
}

```

## To Run Tests

## Lambda Functions

Codes for lambda functions can be found in files called ` lambda1.py ` and ` lambda2.py `.  
You can copy codes directly to your AWS Lambda code window.  
To test you can use example requests above.  

I have omitted `DB_NAME` , `REGION` , `EC2_INSTANCE_ID` and `ARN_OF_SECOND_LAMBDA` for safety reasons. You can replace them with your own.
  
In order to invoke a lambda funtion from another lambda function you need to give related permissions to the invoking lambda.  
You can use policy below to add to your lambda funtion in IAM (AWS Identity and Access Management).

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "*"
        }
    ]
}

```
