'''Sentiment Analysis module for the IBM Watson NLP API'''

import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''This function uses the IBM Watson NLP API to perform sentiment analysis on the input text.'''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}