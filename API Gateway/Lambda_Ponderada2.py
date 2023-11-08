import json

users = {
    "dayllan": "afonso",
}

def lambda_handler(event, context):
    query_parameters = event.get('queryStringParameters', {})
    auth = query_parameters.get('auth', '')

    if not auth:
        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }

    user, password = auth.split(':')

    if user in users and users[user] == password:
        return {
            'statusCode': 200,
            'body': json.dumps(event['body'])
        }
    else:
        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }