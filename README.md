# SWE 599 Project: Cloud Native Application

## To Open The UI
Simply open ` index.html ` file with your browser or run it using you favorite _live server_ extension.  
I have put JavaScript codes and CSS styles inside this single html file. No other dependency to worry about (of course it would not be connected to any backend if you don't have AWS services to back it up).  

I have omitted the ` API_URL ` in the request. It is replaced with the API Gateway URL to access our deployed API. 

## Example Requests

```json 

{
  "amount": 20000,
  "interest": 2.8,
  "maturity": 24,
  "operation": "simple"
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
