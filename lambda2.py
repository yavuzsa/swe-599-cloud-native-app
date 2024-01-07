import json

def lambda_handler(event, context):

    # get message from the first lambda function
    amount = float(event['amount'])
    total_amount = float(event['total_amount'])
    monthly_amount = float(event['monthly_amount'])
    maturity = int(event['maturity'])

    result_string = "Total Amount to be Paid: " + str(total_amount) + "\nBase Amount: " + str(amount) + "\nInterest to be Paid: " + str(total_amount-amount) + "\nMonthly Payment: " + str(monthly_amount)

    return {
    'statusCode': 200,
    'body': json.dumps(result_string)
    }