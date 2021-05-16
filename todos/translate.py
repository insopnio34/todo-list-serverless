import json
import os

from todos import decimalencoder
import boto3
tranductor = boto3.client(service_name='translate')
dynamodb = boto3.resource('dynamodb')



def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    #obtenemos el elemento de la lista
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    #obtenemos el idioma
    idioma= event['pathParameters']['idioma']
    #texto a traducir
    texto=result['Item']['text']
    traduccion = tranductor.translate_text(Text=texto, SourceLanguageCode="es", TargetLanguageCode=idioma)
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(traduccion, cls=decimalencoder.DecimalEncoder)
    }

    return response