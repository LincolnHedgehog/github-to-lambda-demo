import json
def lambda_handler(event, context):
    print('Donw x1.2')
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
