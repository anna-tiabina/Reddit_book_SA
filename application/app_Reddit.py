"""
The app module renders templates for the application, downloads the most popular Reddit reviews and recommends the most popular and positive book review. It contains the following functions:
    *request to render the front page
    *recommendation to render the recommendation page
    *get_sentiment to utilize the tokenizer and the model to predict a class of the review (positive - 1, negative - 0), returns torch.Tensor
    *get_review to connect to Reddit with API, dowload 10 most popular reviews, check their sentiment by calling get_sentiment function and return the first positive review
"""
from flask import Flask
from flask import render_template
from flask import request
import praw
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import numpy as np
import evaluate

app = Flask(__name__)

def get_sentiment(review):
    """The function utilizes the tokenizer and the model to predict a class of the review (positive - 1, negative - 0), returns torch.Tensor"""
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    inputs = tokenizer(review, truncation=True, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    predictions = np.argmax(logits, axis=-1)
    return predictions


def get_review():
    """The function connects to Reddit with API, dowloads 10 most popular reviews, checks their sentiment by calling get_sentiment function and returns the first positive review"""
    reddit = praw.Reddit(
        client_id="client_id",
        client_secret="client_secret",
        refresh_token="refresh_token",
        user_agent="AI recommendations for reading by u/anna_tiabina",
    )
    hot_posts = reddit.subreddit('bookreviewers').hot(limit=10)
    for post in hot_posts: 
        review = post.title + " " + post.selftext
        predictions = get_sentiment(review)
        if predictions == torch.Tensor([1]):
            return review
        else:
            continue


@app.route('/')
def index():
    """The function renders the index page"""
    return render_template('index.html')
 

@app.route('/start')
def start():
    """The function gets the review to be passed to the recommendation template as an argument"""
    review = get_review()
    return recommendation(review)
    

@app.route('/recommendation')
def recommendation(review):
    """The function renders the recommendation page"""
    return render_template('recommendation.html', review = review)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)


