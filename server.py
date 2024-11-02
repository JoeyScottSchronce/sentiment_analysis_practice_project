''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("SentimentAnalyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    to_be_analysed = request.args.get("textToAnalyze")
    response = sentiment_analyzer(to_be_analized)
    label = response['label']
    score = response['score']

    return "The statement was identified as {} with a score of {}.".format(label.split('_')[1, score])

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO

if __name__ == "__main__":
    app.run(debug=True)

    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
