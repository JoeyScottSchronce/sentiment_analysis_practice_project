    
import requests

# Define the URL for the sentiment analysis API
url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

# Set the headers with the required model ID for the API
headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

# Define the first payload with nonsensical text to test the API
myobj = { "raw_document": { "text": "as987da-6s2d aweadsa" } }

# Make a POST request to the API with the first payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the first response
print("Payload 1: ", response.status_code)

# Define the second payload with a meaningful text to test the API
myobj = { "raw_document": { "text": "Testing this application for error handling" } }

# Make a POST request to the API with the second payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the second response
print("Payload 2: ", response.status_code)
 