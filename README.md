## The book recommendation application with Reddit API and DistilBERT fine-tuned on SST-2 as a sentiment analysis tool and notebooks for 

##Table of contents

- Introduction
- Automated labelling and the Cohen’s Kappa coefficient
- Testing and fine-tuning models to choose the most suitable transformer for sentiment analysis 
- PR curves of all models 
- The application
- Project setup


##Introduction

Choosing a book to read can be challenging while dedicated platforms (such as Amazon Books) contain many paid reviews written for marketing purposes, and honest reviews are scattered on social media and difficult to accumulate and use. 

The web application is aimed to provide an independent book recommendation based on a positive review, currently popular on social media, while negative reviews are being dismissed with the help of a sentiment analysis technique. 

Reddit was chosen as the main source of book reviews as this social media promotes anonymization and is less prone to be exploited for marketing purposes than other platforms. Moreover, Reddit provides in-build filtering model to select the most popular post in the subreddit. 

The application and all the files needed for its set-up are stored in the folder "application".

The will work in accordance with the following scenario. When a user clicks the “start” button, the script created a Reddit instance and downloads ten most popular (“hot”) from the Reddit subreddit “book review” via API (calling get_review function), then it checks their sentiment (calling get_sentiment function) one by one in the cycle until it finds a positive book review. The most popular positive review is used as an argument to render the HTML-page. A user sees the most popular positive review.  

The application is hosted on Amazon Web Services and can be accessed via the link https://application-web.st2ff8qfgnvqm.eu-west-1.cs.amazonlightsail.com/ 

##Automated labelling and the Cohen’s Kappa coefficient

As the Reddit reviews proved to be controversial, automated labelling with TextBlob and Afinn as well as labelling by the second annotator and calculating the Cohen’s Kappa coefficient were introduced.

##Testing and fine-tuning models to choose the most suitable transformer for sentiment analysis 

DistilBERT, DistilRoBERTa, XLNet, GPT-2 were fine-tuned on the dataset of Reddit book reviews (training dataset) and check point of the models fine-tuned on the SST-2 (Stanford Sentiment Treebank) were downloaded from the Hugging Face repository. Hence, in total, 6 versions were tested in the experimental phase: DistilBERT, DistilRoBERTa, XLNet, GPT-2 fine-tuned on SST-2 and the same models fine-tuned on the training dataset.

The experimental findings indicated that the DistilBERT model fine-tuned on SST-2 dataset exhibited the best performance on the testing dataset consisting of Reddit book reviews. These results can be   explained by the fact that sentiment analysis is more natural application for BERT models and the specific features of the model such as its pre-training objectives, context grasping, architecture, number of layers and parameters.

##PR curves of all models 

The precision recall curves of all models are plotted against each other while using different confidence thresholds (from 0 to 1) to analyse how well they detect positive reviews without misclassifying negative ones. DistilBERT model fine-tuned on SST-2 preforms better than others almost with any threshold. 

##Ensuring that the model is not biased with SHapley Additive exPlanations

The model`s predictions were interpreted with the (SHapley Additive exPlanations) technique to ensure that the model was not biased towards certain words and an optimal confidence threshold, based on the precision–recall curve, is introduced to ensure that the model handle controversial reviews properly. 


##The application 


#General description


The selection of the technologies for the application is determine by three main functional requirements. The application must connect to Reddit via API to download a popular book review. The application must have user-friendly graphic web interface to display the popular book review. The application must apply the chosen model to define sentiment of the review to display only positive one. 

To meet these requirements, Python Flask web-framework will be used to render HTML-templates styled with CSS-styles, Python unittest and pytest to test the application. 

As far as Reddit API is concerned, authenticating via OAuth will be used as advised by Reddit (Reddit, 2025c). The application is registered in the Reddit developer`s account  to receive a permanent refreshed token and the access to the prawn library, the Python library API wrapper . The praw library will be used to create an instance of Reddit and download the data required for the application. 

In addition to that, Docker (Docker, 2025) and Amazon Web Services Lightsail (Amazon Web Services, 2025a) will be used to create an image of a container and to host the application on cloud.

#Modules of the application

The app module renders templates for the application, downloads the most popular Reddit reviews and recommends the most popular and positive book review. It contains the following functions:
    *request to render the front page
    *recommendation to render the recommendation page
    *get_sentiment to utilize the tokenizer and the model to predict a class of the review (positive - 1, negative - 0), returns torch.Tensor
    *get_review to connect to Reddit with API, dowload 10 most popular reviews, check their sentiment by calling get_sentiment function and return the first positive review

The pytest module allows a developer to test the application (app_Reddit), namely its functions which render the HTML pages. It contains the following functions:
    *test_index to test rendering of the respective page 
    *test_start to test rendering of the respective page 

The unittest module allows a developer to test the module app_Reddit, namely, if its functions dowload and process the data correctly. It contains the following functions:
    *test_get_review tests wheather a review is dowloaded from Reddit
    *test_get_sentiment tests whether the sentiment model works properly. The testing review is positive and the function get_sentiment should return the prediction equal to  np.array([1])



##Project setup

There is the compose.yaml, Dockerfile and the requirements file used for the Docker container.

Requirements: 
aiohappyeyeballs==2.4.4
aiohttp==3.11.11
aiosignal==1.3.2
attrs==24.3.0
blinker==1.9.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
datasets==3.2.0
dill==0.3.8
evaluate==0.4.3
filelock==3.16.1
Flask==3.1.0
frozenlist==1.5.0
fsspec==2024.9.0
huggingface-hub==0.27.1
idna==3.10
iniconfig==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
joblib==1.4.2
MarkupSafe==3.0.2
mpmath==1.3.0
multidict==6.1.0
multiprocess==0.70.16
networkx==3.4.2
nltk==3.9.1
numpy==2.2.1
packaging==24.2
pandas==2.2.3
pip==23.2.1
pluggy==1.5.0
praw==7.8.1
prawcore==2.4.0
propcache==0.2.1
pyarrow==19.0.0
pytest==8.3.4
python-dateutil==2.9.0.post0
pytz==2024.2
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
safetensors==0.5.2
scipy==1.15.2
setuptools==65.5.0
six==1.17.0
sympy==1.13.1
textblob==0.18.0.post0
tokenizers==0.21.0
torch==2.5.1
tqdm==4.67.1
transformers==4.48.0
typing_extensions==4.12.2
tzdata==2024.2
update-checker==0.18.0
urllib3==2.2.3
websocket-client==1.8.0
Werkzeug==3.1.3
xxhash==3.5.0
yarl==1.18.3


How to run an application:
1. If downloaded from GitHub, the folder "application" contains the  compose.yaml, Dockerfile and the requirements.txt files to build and run the application. In the Docker terminal, one should go to the folder with app_Reddit.py and execute the following command:  docker compose up
The application will be run on a local host http://127.0.0.1:5000/ 
2. A user can install the required environment manually (the requirements are listed in the file requirements file), go to the folder with CCB in Command Prompt and (if the required tools mentioned above are installed and all the modules and parts of the application correctly downloaded) execute the following commands: set FLASK_APP=app_Reddit.py and flask run. The application will be on the local host http://127.0.0.1:5000/

The application can be reached via amazonlightsail.com (https://application-web.st2ff8qfgnvqm.eu-west-1.cs.amazonlightsail.com/ ), if CCB is deployed.








