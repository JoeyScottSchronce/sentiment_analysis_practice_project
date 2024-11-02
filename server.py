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
    try:
        # Get the text from the request
        textToAnalyze = request.args.get("textToAnalyze")
        if not textToAnalyze:
            raise ValueError("No text provided for analysis.")
        
        # Call the sentiment analysis function
        response = sentiment_analyzer(textToAnalyze)
        
        # Ensure response has expected keys
        label = response.get('label')
        score = response.get('score')
        if label is None or score is None:
            raise ValueError("Invalid response from sentiment analysis.")
        
        # Format and return the result
        label_part = label.split('_')[1]  # Try to split label
        return f"The statement was identified as {label_part} with a score of {score}."
    
    except KeyError as e:
        return f"Error: Missing expected key in response: {e}", 400
    except IndexError:
        return "Error: Unexpected format in label string; unable to split.", 400
    except ValueError as e:
        return f"Error: {str(e)}", 400
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500

@app.route("/")
def render_index_page():
    return render_template('index.html')
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
