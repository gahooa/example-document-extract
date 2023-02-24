# vim:fileencoding=utf-8:ts=4:sw=4:sts=4:expandtab


import os
import openai
import requests
import sys
from rich.pretty import pprint
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")


import boto3


textract_client = boto3.client('textract')

# Open the input.pdf file and read the contents as bytes
with open('input.png', 'rb') as file:
    pdf_data = file.read()


# Call the Textract API to analyze the PDF document
response = textract_client.analyze_document(Document={'Bytes': pdf_data}, FeatureTypes=['TABLES'])

#pprint(response)


# Extract the text from the response
text = ''
for item in response['Blocks']:
    if item['BlockType'] == 'LINE':
        text += item['Text'] + '\n'


# Print the extracted text
#print(text)


text_data = text.strip()


instructions = '''
Produce a json list of objects, each containing 'transaction_date', 'transaction_name', 'amount'.  
Dates should be yyyy-mm-dd format.
Numbers should be strings.
Do not use dollar sign in the numeric values.
'''


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text_data + '\n---\n\n' + instructions,
  temperature=0,
  max_tokens=1308,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
)

print(t := response['choices'][0]['text'])

import json
pprint(json.loads(t))


